from django.urls import path
from . import views

urlpatterns = [
     path("", views.ReviewView.as_view()),
     # *NOTES*
     # This line defines a URL pattern for the root URL ("/").
     # It uses the `ReviewView` class-based view and calls its `as_view` method to convert it into a view function.
     # https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#using-class-based-views

     path("thank-you", views.ThankYouView.as_view()),
     # *NOTES*
     # This line defines a URL pattern for the "thank-you" page ("/thank-you").
     # It uses the `ThankYouView` class-based view and calls its `as_view` method to convert it into a view function.
     # https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#using-class-based-views

     path("reviews", views.ReviewsListView.as_view()),
     # *NOTES*
     # This line defines a URL pattern for the "reviews" page ("/reviews").
     # It uses the `ReviewsListView` class-based view and calls its `as_view` method to convert it into a view function.
     # https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#using-class-based-views

     path("reviews/<int:pk>", views.SingleReviewView.as_view())
     # *NOTES*
     # This line defines a URL pattern for the single review page ("/reviews/<int:pk>").
     # The `<int:pk>` part is a path converter that captures an integer value and passes it to the view as a `pk` parameter.
     # It uses the `SingleReviewView` class-based view and calls its `as_view` method to convert it into a view function.
     # https://docs.djangoproject.com/en/5.0/topics/http/urls/#path-converters
]
