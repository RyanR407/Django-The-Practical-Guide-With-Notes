from reviews.models import Review
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.


class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context
    # *NOTES*
    # This method overrides `get_context_data` to add additional context to the template.
    # It first calls the parent class's `get_context_data` method to ensure the base context is included.
    # It retrieves the currently loaded review object using `self.object`.
    # It accesses the current request object using `self.request`.
    # It attempts to retrieve the `favorite_review` value from the session using `request.session.get("favorite_review")`.
    # The `context["is_favorite"]` variable is set to `True` if the `favorite_review` in the session matches the current review's ID, indicating that this review is the user's favorite.
    # This additional context is then passed to the template to conditionally display content.
    # Sessions in Django are used to store data for a particular user across multiple requests. 
    # The session framework lets you store and retrieve arbitrary data based on the user's session ID.
    # Sessions are often used for user login state, shopping carts, user preferences, and other user-specific data.
    # https://docs.djangoproject.com/en/5.0/topics/http/sessions/
    # https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_context_data
    # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.session

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
    # *NOTES*
    # This view handles POST requests to add a review to the favorites.
    # It overrides the `post` method of the base `View` class to handle form submissions.
    # It retrieves the `review_id` from the POST data using `request.POST["review_id"]`.
    # The `review_id` is then stored in the session under the key `favorite_review`.
    # The session framework allows you to store arbitrary data about the user on the server.
    # Storing the `review_id` in the session makes it persist across multiple requests and can be accessed later.
    # After storing the `review_id` in the session, the user is redirected to the detail view of the favorite review using `HttpResponseRedirect`.
    # `HttpResponseRedirect` is used to perform a temporary redirect to the specified URL.
    # Sessions in Django are commonly used to manage user-specific data, such as login states, shopping carts, and user preferences.
    # This approach allows for seamless user experience by maintaining state information across different views.
    # https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#handling-forms-with-class-based-views
    # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseRedirect
    # https://docs.djangoproject.com/en/5.0/topics/http/sessions/
