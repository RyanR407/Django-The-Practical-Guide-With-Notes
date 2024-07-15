from django import forms

class ProfileForm(forms.Form):
    user_image = forms.ImageField()
# *NOTES*
# This line defines an `ImageField` for the `ProfileForm`.
# `ImageField` is a file field for uploading image files.
# https://docs.djangoproject.com/en/3.1/ref/forms/fields/#imagefield