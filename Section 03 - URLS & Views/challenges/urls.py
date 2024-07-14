from django.urls import path
# *NOTES*
# This line imports the `path` function from the `django.urls` module.
# The `path` function is used to define URL patterns in Django.
# https://docs.djangoproject.com/en/5.0/topics/http/urls/#path

from . import views
# *NOTES*
# This line imports the `views` module from the current package.
# The `views` module will contain the view functions that handle the logic for each URL pattern.
# https://docs.djangoproject.com/en/5.0/topics/http/views/

urlpatterns = [
    # *NOTES*
    # The `urlpatterns` list is a sequence of URL patterns to be matched against the incoming request URLs.
    # Each pattern is defined using the `path` function.
    # https://docs.djangoproject.com/en/5.0/topics/http/urls/#how-django-processes-a-request

    path("", views.index), # /challenges/
    # *NOTES*
    # This URL pattern matches the root URL of the `challenges` app.
    # When the URL is `/challenges/`, the `index` view function will be called.
    # https://docs.djangoproject.com/en/5.0/topics/http/urls/#path-argument

    path("<int:month>", views.monthly_challenge_by_number),
    # *NOTES*
    # This URL pattern matches URLs like `/challenges/1/`, `/challenges/2/`, etc.
    # The `<int:month>` part captures an integer from the URL and passes it as an argument to the `monthly_challenge_by_number` view function.
    # https://docs.djangoproject.com/en/5.0/topics/http/urls/#path-converters

    path("<str:month>", views.monthly_challenge, name="month-challenge")
    # *NOTES*
    # This URL pattern matches URLs like `/challenges/january/`, `/challenges/february/`, etc.
    # The `<str:month>` part captures a string from the URL and passes it as an argument to the `monthly_challenge` view function.
    # The `name="month-challenge"` part assigns a name to this URL pattern, allowing it to be referenced elsewhere in the project.
    # https://docs.djangoproject.com/en/5.0/topics/http/urls/#naming-url-patterns
]
