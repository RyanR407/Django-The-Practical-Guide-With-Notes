from django import forms
from .models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
#         "required": "Your name must not be empty!",
#         "max_length": "Please enter a shorter name!"
#     })
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
# *NOTES*
# This block defines a `ReviewForm` class, which is a standard Django form (not model-based).
# The `user_name` field is a `CharField` with a maximum length of 100 and custom error messages.
# The `review_text` field is a `CharField` with a `Textarea` widget and a maximum length of 200.
# The `rating` field is an `IntegerField` with minimum and maximum values set to 1 and 5, respectively.
# https://docs.djangoproject.com/en/5.0/ref/forms/fields/#charfield
# https://docs.djangoproject.com/en/5.0/ref/forms/fields/#integerfield
# https://docs.djangoproject.com/en/5.0/ref/forms/widgets/#django.forms.Textarea


class ReviewForm(forms.ModelForm):
    # *NOTES*
    # This line defines a `ReviewForm` class, which is a model-based form.
    # The form fields are automatically generated based on the `Review` model.
    # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/

    class Meta:
        model = Review
        # *NOTES*
        # This line specifies the model that the form is based on, which is the `Review` model.
        # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#django.forms.ModelForm.Meta.model

        fields = "__all__"
        # *NOTES*
        # This line specifies that all fields from the `Review` model should be included in the form.
        # An alternative is to use the `exclude` option to exclude specific fields from the form.
        # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#selecting-the-fields-to-use

        # exclude = ['owner_comment']
        # *NOTES*
        # This line (commented out) would exclude the `owner_comment` field from the form if uncommented.
        # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#django.forms.ModelForm.Meta.exclude

        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }
        # *NOTES*
        # This dictionary defines custom labels for the form fields.
        # The keys are the model field names, and the values are the custom labels.
        # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#overriding-the-default-fields

        error_messages = {
            "user_name": {
              "required": "Your name must not be empty!",
              "max_length": "Please enter a shorter name!"
            }
        }
        # *NOTES*
        # This dictionary defines custom error messages for the `user_name` field.
        # The keys are the error types, and the values are the custom error messages.
        # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#overriding-the-default-fields
