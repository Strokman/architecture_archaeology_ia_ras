# from celery import shared_task
# from architecture_archaeology import settings

# def test_func(name):
#     print(name)
# @shared_task(name='TESTTEST')
# def test_task(name):
#     test_func(name)
#     return name

# def upload(self):
#     self = self['file']
#     self.client.put_object(Body=self.file.file.read(),
#                         Bucket=settings.BUCKET,
#                         Key=self.file.object_storage_key,
#                         )
    
#     print(f'Uploaded {self}')
# @shared_task(name='TESTTEST2')
# def test_task2(obj):
#     upload(obj)