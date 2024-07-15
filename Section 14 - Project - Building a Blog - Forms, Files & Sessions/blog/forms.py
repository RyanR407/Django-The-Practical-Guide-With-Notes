from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
          "user_name": "Your Name",
          "user_email": "Your Email",
          "text": "Your Comment"
        }
# *NOTES*
# `CommentForm` is a `ModelForm` for the `Comment` model.
# The `Meta` class defines the model to use and the fields to exclude (`post`).
# The `labels` attribute specifies custom labels for form fields.
# https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#modelform
