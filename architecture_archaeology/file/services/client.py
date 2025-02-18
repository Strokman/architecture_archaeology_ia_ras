import boto3

import architecture_archaeology.settings as settings


def create_s3_client():
    """
    Создание клиента соединения с S3
    """
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        region_name='ru-central1',
        endpoint_url=settings.OBJECT_STORAGE_URL
    )

    return s3
