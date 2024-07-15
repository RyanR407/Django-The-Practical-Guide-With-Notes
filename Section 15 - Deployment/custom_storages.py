from django.conf import settings
# *NOTES*
# This line imports the `settings` module from `django.conf`.
# The `settings` module allows access to Django project settings.
# https://docs.djangoproject.com/en/5.0/topics/settings/

from storages.backends.s3boto3 import S3Boto3Storage
# *NOTES*
# This line imports the `S3Boto3Storage` class from `storages.backends.s3boto3`.
# `S3Boto3Storage` is a storage backend for storing files in an Amazon S3 bucket.
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html

class StaticFileStorage(S3Boto3Storage):
    location = settings.STATICFILES_FOLDER
    # *NOTES*
    # This class defines a custom storage backend for static files using Amazon S3.
    # The `location` attribute is set to the value of `STATICFILES_FOLDER` from the Django settings.
    # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#setting-parameters

class MediaFileStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_FOLDER
    # *NOTES*
    # This class defines a custom storage backend for media files using Amazon S3.
    # The `location` attribute is set to the value of `MEDIAFILES_FOLDER` from the Django settings.
    # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#setting-parameters
