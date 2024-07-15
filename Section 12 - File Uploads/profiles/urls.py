from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    # *NOTES*
    # This line defines a URL pattern that maps the root URL to the `CreateProfileView` view.
    # The `as_view()` method returns a callable view that can be used in the URLconf.
    # https://docs.djangoproject.com/en/3.1/topics/http/urls/#path

    path("list", views.ProfilesView.as_view())
    # *NOTES*
    # This line defines a URL pattern that maps the "list" URL to the `ProfilesView` view.
    # The `as_view()` method returns a callable view that can be used in the URLconf.
    # https://docs.djangoproject.com/en/3.1/topics/http/urls/#path
]
