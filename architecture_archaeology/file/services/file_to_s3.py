from .client import create_s3_client
import architecture_archaeology.settings as settings


def upload_file_to_s3(file, filename):
    client = create_s3_client()
    client.put_object(Body=file.read(),
                      Bucket=settings.BUCKET,
                      Key=f'{filename}')
    return True
