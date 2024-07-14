from reviews.models import Review
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views import View
# *NOTES*
# This line imports the `View` class from `django.views`.
# `View` is a base class for all class-based views in Django.
# https://docs.djangoproject.com/en/5.0/topics/class-based-views/

from .forms import ReviewForm
# *NOTES*
# This line imports the `ReviewForm` class from the current app's `forms` module.
# The `ReviewForm` class is used to create and handle the review form.
# https://docs.djangoproject.com/en/5.0/topics/forms/

# Create your views here.


class ReviewView(View):
    def get(self, request):
        # *NOTES*
        # This method handles GET requests to the `ReviewView`.
        # It initializes a new `ReviewForm` and renders the `review.html` template with the form.
        # https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#handling-get-and-post-requests

        form = ReviewForm()
        # *NOTES*
        # This line initializes a new instance of the `ReviewForm`.
        # The form is empty because no data is passed to it.
        # https://docs.djangoproject.com/en/5.0/topics/forms/#using-forms

        return render(request, "reviews/review.html", {
            "form": form
        })
        # *NOTES*
        # This line renders the `review.html` template with the context containing the form.
        # The `render` function takes the request, template name, and context as arguments and returns an HttpResponse.
        # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render

    def post(self, request):
        # *NOTES*
        # This method handles POST requests to the `ReviewView`.
        # It processes the form submission and saves the data if the form is valid.
        # https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#handling-get-and-post-requests

        form = ReviewForm(request.POST)
        # *NOTES*
        # This line initializes a new instance of the `ReviewForm` with the POST data.
        # The form is populated with the data submitted by the user.
        # https://docs.djangoproject.com/en/5.0/topics/forms/#using-forms

        if form.is_valid():
            # *NOTES*
            # This line checks if the form is valid.
            # The `is_valid` method performs validation on the form fields.
            # https://docs.djangoproject.com/en/5.0/ref/forms/api/#django.forms.Form.is_valid

            form.save()
            # *NOTES*
            # This line saves the form data to the database.
            # The `save` method creates a new `Review` object with the form data and saves it to the database.
            # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#the-save-method

            return HttpResponseRedirect("/thank-you")
            # *NOTES*
            # This line redirects the user to the "thank-you" page after successfully saving the form data.
            # `HttpResponseRedirect` is used to perform the redirection.
            # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseRedirect

        return render(request, "reviews/review.html", {
            "form": form
        })
        # *NOTES*
        # If the form is not valid, this line re-renders the `review.html` template with the form (including errors).
        # The `render` function takes the request, template name, and context as arguments and returns an HttpResponse.
        # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render

def thank_you(request):
    return render(request, "reviews/thank_you.html")