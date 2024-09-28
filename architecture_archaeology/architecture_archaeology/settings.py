"""
Django settings for architecture_archaeology project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta

from dotenv import load_dotenv
from os import path, environ


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


load_dotenv(path.join(BASE_DIR.parent.absolute(), '.env'))

PROJECT = 'architecture_archaeology'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(environ.get('DEBUG', 0))

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'testserver', 'base-habilis.ru', '185.70.185.20']

# Application definition

INSTALLED_APPS = [
    'arch_site.apps.ArchSiteConfig',
    'artefact.apps.ArtefactConfig',
    'helpers.apps.HelpersConfig',
    'building.apps.BuildingConfig',
    'index.apps.IndexConfig',
    'artwork.apps.ArtworkConfig',
    'file.apps.FileConfig',
    'map.apps.MapConfig',
    'measurement.apps.MeasurementConfig',
    "debug_toolbar",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'django_filters',
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=100),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

CSRF_TRUSTED_ORIGINS = ['https://data.archaeolog.ru']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "core.filesize_middleware.FileSizeMiddleware"
]

ROOT_URLCONF = 'architecture_archaeology.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {'settings_value': 'helpers.templatetags.settings_value'}
        },
    },
]

WSGI_APPLICATION = 'architecture_archaeology.wsgi.application'

SESSION_COOKIE_AGE = 60 * 60 + 24

SESSION_SAVE_EVERY_REQUEST = True

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ.get('POSTGRES_DB'),
        'HOST': environ.get('POSTGRES_HOST'),
        'USER': environ.get('POSTGRES_USER'),
        'PASSWORD': environ.get('POSTGRES_PASSWORD'),
        'PORT': environ.get('POSTGRES_PORT'),
        'ATOMIC_REQUESTS': True,
        "TEST": {
            "NAME": "aa-testdb",
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

INTERNAL_IPS = [
    "127.0.0.1",
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

# DATA_UPLOAD_MAX_NUMBER_FILES = 2

USE_I18N = True

USE_TZ = True

GMAPS_API_KEY = environ.get('GMAPS_API_KEY')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]
STATIC_ROOT = "staticfiles"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{name}:{levelname}:{asctime}:{funcName}:{message}",
            "datefmt": '%Y-%m-%d %H-%M-%S',
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "simple": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "simple_prod": {
            "level": "DEBUG",
            "filters": ["require_debug_false"],
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        'console_on_not_debug': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        # "mail_admins": {
        #     "level": "ERROR",
        #     "class": "django.utils.log.AdminEmailHandler",
        #     "filters": ["special"],
        # },
    },
    "loggers": {
        "django": {
            "handlers": ["simple"],
            "propagate": True,
        },
        # "django.server": {
        #     "handlers": ["console_simple"],
        #     "level": "INFO",
        #     "propagate": False,
        # },
        PROJECT: {
            "handlers": ["console", 'console_on_not_debug'],
            "level": "INFO"
        },
    },
}
LOGIN_REDIRECT_URL = '/'


DATETIME_INPUT_FORMATS = [
    "%Y-%m-%d %H:%M:%S",  # '2006-10-25 14:30:59'
    "%Y-%m-%d %H:%M:%S.%f",  # '2006-10-25 14:30:59.000200'
    "%Y-%m-%d %H:%M",  # '2006-10-25 14:30'
    "%m/%d/%Y %H:%M:%S",  # '10/25/2006 14:30:59'
    "%m/%d/%Y %H:%M:%S.%f",  # '10/25/2006 14:30:59.000200'
    "%m/%d/%Y %H:%M",  # '10/25/2006 14:30'
    "%m/%d/%y %H:%M:%S",  # '10/25/06 14:30:59'
    "%m/%d/%y %H:%M:%S.%f",  # '10/25/06 14:30:59.000200'
    "%m/%d/%y %H:%M",  # '10/25/06 14:30'
    "%d-%m-%Y",
    '%Y-%m-%d'
]

# Cache settings

REDIS_HOST = environ.get('REDIS_HOST', 'localhost')


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:6379",
        'TIMEOUT': 120,
    }
}

DEFAULT_TIMEOUT = 60 * 60 * 24
DEFAULT_IMAGE_TIMEOUT = 60 * 60 * 24 * 365

# Celery settings
CELERY_BROKER_URL = f'redis://{REDIS_HOST}:6379/0'

# Yandex cloud S3 config params

OBJECT_STORAGE_URL = environ.get('OBJECT_STORAGE_URL')

BUCKET = environ.get('BUCKET')

AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')

AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')

YMAPS_TOKEN = environ.get('YMAPS_TOKEN')

# Mail settings

EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD')
EMAIL_HOST = environ.get('EMAIL_HOST')
EMAIL_PORT = environ.get('EMAIL_PORT')
EMAIL_USE_SSL = environ.get('EMAIL_USE_SSL')
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER')
DEFAULT_FROM_EMAIL = 'arch-frescos@yandex.ru'