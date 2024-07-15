from django.urls import path

from . import views

urlpatterns = [
     path("", views.ReviewView.as_view()),
     path("thank-you", views.ThankYouView.as_view()),
     path("reviews", views.ReviewsListView.as_view()),
     path("reviews/favorite", views.AddFavoriteView.as_view()),
     # *NOTES*
     # This URL pattern maps the "reviews/favorite" URL to the `AddFavoriteView` view.
     # The `as_view()` method converts the class-based view into a callable view function.
     # https://docs.djangoproject.com/en/3.1/topics/http/urls/#path
     path("reviews/<int:pk>", views.SingleReviewView.as_view())
]
