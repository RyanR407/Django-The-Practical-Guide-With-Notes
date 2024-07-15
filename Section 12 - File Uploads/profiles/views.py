from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .forms import ProfileForm
from .models import UserProfile

# Create your views here

class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"
    # *NOTES*
    # `CreateProfileView` is a class-based view for creating a `UserProfile` instance.
    # It inherits from `CreateView`, which provides a way to display and process a form for creating an object.
    # `template_name` specifies the template to use for rendering the view. In this case, it uses `profiles/create_profile.html`.
    # `model` specifies the model to use for the view. Here, it uses the `UserProfile` model.
    # `fields` specifies the fields to include in the form. Using `"__all__"` includes all fields of the model in the form.
    # `success_url` specifies the URL to redirect to upon successful form submission. Here, it redirects to `/profiles`.
    # The `CreateView` automatically handles the form display and processing logic, including form validation and saving the form data to the database.
    # https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-editing/#createview

class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"
    # *NOTES*
    # `ProfilesView` is a class-based view for displaying a list of `UserProfile` instances.
    # It inherits from `ListView`, which provides a way to display a list of objects.
    # `model` specifies the model to use for the view. Here, it uses the `UserProfile` model.
    # `template_name` specifies the template to use for rendering the view. In this case, it uses `profiles/user_profiles.html`.
    # `context_object_name` specifies the context variable name for the list of objects. The list of `UserProfile` instances will be accessible in the template using the name `profiles`.
    # The `ListView` automatically handles retrieving the list of objects from the database and rendering the specified template with the list of objects.
    # https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#listview