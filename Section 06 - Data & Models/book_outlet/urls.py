from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("<slug:slug>", views.book_detail, name="book-detail")
    # *NOTES*
    # This line defines a URL pattern that captures a slug parameter from the URL and maps it to the `book_detail` view.
    # The `"<slug:slug>"` part captures a slug from the URL and passes it to the view as a keyword argument named `slug`.
    # The `views.book_detail` specifies the view function to handle this URL pattern.
    # The `name="book-detail"` argument assigns a name to this URL pattern, allowing it to be referenced by name elsewhere in the project.
    # https://docs.djangoproject.com/en/5.0/topics/http/urls/#path
    # https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.path

]
