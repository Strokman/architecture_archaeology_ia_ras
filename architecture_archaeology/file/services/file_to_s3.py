from logging import getLogger
from .client import create_s3_client
from botocore.exceptions import ClientError
import architecture_archaeology.settings as settings
from helpers.timer import timer
import threading


class S3FileHandler:

    def __init__(self, file):
        self.client = create_s3_client()
        self.file = file
        self.logger = getLogger(
            settings.PROJECT + '.' + self.__class__.__name__
            )

    @timer
    def upload_file_to_s3(self):
        t = threading.Thread(target=self.upload)
        t.start()
        self.logger.info(
            f'{self.file.object_storage_key} successfully uploaded to object storage')

    def get_file_from_s3(self):
        try:
            get_object_response = self.client.get_object(
                Bucket=settings.BUCKET,
                Key=self.file.object_storage_key
                )
            self.logger.info(
                f'{self.file.object_storage_key} successfully downloaded from object storage')       
            return get_object_response['Body']
        except ClientError as e:
            self.logger.error(e)

    def delete_file_from_s3(self):
        try:
            self.client.delete_object(Bucket=settings.BUCKET,
                                    Key=self.file.object_storage_key)
            self.logger.warning(f'{self.file.object_storage_key} deleted from object storage')
        except ClientError as e:
            self.logger.error(e)
        return True

    def upload(self):
        self.client.put_object(Body=self.file.file.read(),
                        Bucket=settings.BUCKET,
                        Key=self.file.object_storage_key,
                        )
