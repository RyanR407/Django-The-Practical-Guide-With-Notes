from django.db import models

# Create your models here.

class UserProfile(models.Model):
    image = models.ImageField(upload_to="images")
# *NOTES*
# This line defines an `ImageField` for the `UserProfile` model.
# The `upload_to` argument specifies the directory within `MEDIA_ROOT` where uploaded files will be stored.
# https://docs.djangoproject.com/en/3.1/ref/models/fields/#imagefield