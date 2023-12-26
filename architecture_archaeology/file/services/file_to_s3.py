from .client import create_s3_client
import architecture_archaeology.settings as settings
from file.services import FileHandler
from file.models import File


class S3FileHandler:

    def __init__(self, file: FileHandler | File):
        self.client = create_s3_client()
        self.file = file

    def upload_file_to_s3(self):
        self.client.put_object(Body=self.file.file.read(),
                        Bucket=settings.BUCKET,
                        Key=self.file.object_storage_key)
        return True

    def get_file_from_s3(self):
        get_object_response = self.client.get_object(Bucket=settings.BUCKET,
                                                    Key=self.file.object_storage_key)
        return get_object_response['Body']

    def delete_file_from_s3(self):
        self.client.delete_object(Bucket=settings.BUCKET,
                                Key=self.file.object_storage_key)
        return True
