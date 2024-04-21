from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings


class FileSizeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request method is POST and contains files
        if request.method == 'POST' and request.FILES:
            print(request.FILES)
            # Get the maximum allowed file size from settings, default to 10MB if not set
            max_file_size = getattr(settings, 'MAX_FILE_UPLOAD_SIZE', 40 * 1024 * 1024)  # Default to 40MB
            for file_field in request.FILES.values():
                # Check if the file size exceeds the maximum allowed size
                if file_field.size > max_file_size:
                    messages.error(request, 'Файл слишком большого размера')
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        return self.get_response(request)