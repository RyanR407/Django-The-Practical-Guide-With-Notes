from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
# *NOTES*
# This line imports `Http404`, `HttpResponseNotFound`, and `HttpResponseRedirect` classes from `django.http`.
# `Http404` is used to raise a 404 not found exception.
# https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.http.Http404

from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
}
# *NOTES*
# The value for "december" has been changed to `None` to represent that there is no challenge for December.

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })
    # *NOTES*
    # This line renders the `index.html` template with the `months` context.
    # The `render` function combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
        # *NOTES*
        # This line renders the `challenge.html` template with the `text` and `month_name` context.
        # The `render` function combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
        # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render
    except KeyError:
        # *NOTES*
        # Catch a `KeyError` exception if the month is not found in the `monthly_challenges` dictionary.

        raise Http404()
        # *NOTES*
        # Raise an `Http404` exception if the month is not found.
        # This is a more appropriate way to handle not found pages in Django.
        # https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.http.Http404
