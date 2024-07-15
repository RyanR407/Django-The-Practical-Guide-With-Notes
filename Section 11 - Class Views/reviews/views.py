from reviews.models import Review
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from django.views.generic.base import TemplateView
# *NOTES*
# This line imports the `TemplateView` class from `django.views.generic.base`.
# `TemplateView` is a class-based view for rendering a template.
# https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#templateview

from django.views.generic import ListView, DetailView
# *NOTES*
# This line imports the `ListView` and `DetailView` classes from `django.views.generic`.
# `ListView` is a class-based view for displaying a list of objects.
# `DetailView` is a class-based view for displaying a detail page for a single object.
# https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#listview
# https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#detailview

from django.views.generic.edit import CreateView
# *NOTES*
# This line imports the `CreateView` class from `django.views.generic.edit`.
# `CreateView` is a class-based view for creating a new object.
# https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-editing/#createview

from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    # *NOTES*
    # This class defines a `ReviewView` that inherits from `CreateView`.
    # The `model` attribute specifies the model to use (`Review`).
    # The `form_class` attribute specifies the form class to use (`ReviewForm`).
    # The `template_name` attribute specifies the template to render (`reviews/review.html`).
    # The `success_url` attribute specifies the URL to redirect to upon successful form submission.
    # `CreateView` handles the form display, validation, and saving the form data to the database.
    # https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-editing/#createview

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    # *NOTES*
    # This class defines a `ThankYouView` that inherits from `TemplateView`.
    # The `template_name` attribute specifies the template to render (`reviews/thank_you.html`).
    # `TemplateView` is used to render a template without needing to provide additional context or processing.
    # https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#templateview

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context
    # *NOTES*
    # This method overrides the `get_context_data` method to add extra context data.
    # The `super().get_context_data(**kwargs)` call retrieves the existing context data.
    # The `context["message"]` line adds a new key-value pair to the context.
    # `get_context_data` allows you to pass additional data to the template.
    # https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.get_context_data

class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"
    # *NOTES*
    # This class defines a `ReviewsListView` that inherits from `ListView`.
    # The `template_name` attribute specifies the template to render (`reviews/review_list.html`).
    # The `model` attribute specifies the model to use (`Review`).
    # The `context_object_name` attribute specifies the name of the context variable to use for the list of objects (`reviews`).
    # `ListView` automatically retrieves a list of objects from the database and renders the specified template with the list of objects.
    # https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#listview
    
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data
    # *NOTES*
    # This method overrides the `get_queryset` method to filter the queryset.
    # The `super().get_queryset()` call retrieves the existing queryset.
    # The `base_query.filter(rating__gt=4)` line filters the queryset to include only reviews with a rating greater than 4.
    # This code is commented out and not currently active.
    # https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#listview

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    # *NOTES*
    # This class defines a `SingleReviewView` that inherits from `DetailView`.
    # The `template_name` attribute specifies the template to render (`reviews/single_review.html`).
    # The `model` attribute specifies the model to use (`Review`).
    # `DetailView` retrieves a single object from the database and renders the specified template with the object's details.
    # https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#detailview
