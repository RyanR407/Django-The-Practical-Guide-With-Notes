from django.shortcuts import render
# *NOTES*
# This line imports the `render` function from `django.shortcuts`.
# The `render` function is used to render a template with a context.
# https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# *NOTES*
# These lines import `HttpResponse`, `HttpResponseNotFound`, and `HttpResponseRedirect` classes from `django.http`.
# `HttpResponse` is used to return a simple HTTP response.
# `HttpResponseNotFound` is used to return a 404 not found response.
# `HttpResponseRedirect` is used to redirect to a different URL.
# https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse
# https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseNotFound
# https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseRedirect

from django.urls import reverse
# *NOTES*
# This line imports the `reverse` function from `django.urls`.
# The `reverse` function is used to reverse-resolve URL names into URL paths.
# https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.reverse

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
    "december": "Learn Django for at least 20 minutes every day!"
}
# *NOTES*
# This dictionary `monthly_challenges` stores the challenges for each month.
# The keys are the month names, and the values are the corresponding challenge descriptions.

# Create your views here.
# *NOTES*
# This is a placeholder comment suggesting where to define view functions.
# View functions handle HTTP requests and return HTTP responses.

def index(request):
    # *NOTES*
    # This defines the `index` view function which handles requests to the root URL of the `challenges` app.
    # The `request` parameter is an HttpRequest object representing the current request.
    # https://docs.djangoproject.com/en/5.0/topics/http/views/

    list_items = ""
    # *NOTES*
    # Initialize an empty string `list_items` to store the HTML list items.

    months = list(monthly_challenges.keys())
    # *NOTES*
    # Get a list of all month names from the `monthly_challenges` dictionary keys.

    for month in months:
        # *NOTES*
        # Iterate over each month in the `months` list.

        capitalized_month = month.capitalize()
        # *NOTES*
        # Capitalize the first letter of the month name.

        month_path = reverse("month-challenge", args=[month])
        # *NOTES*
        # Use the `reverse` function to get the URL path for the `month-challenge` view.
        # The `args` parameter specifies the arguments to pass to the URL pattern.
        # https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.reverse

        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
        # *NOTES*
        # Append an HTML list item with a link to the `month_path` to the `list_items` string.

    # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."
    # *NOTES*
    # This is a comment showing an example of what the `list_items` string will look like after the loop.

    response_data = f"<ul>{list_items}</ul>"
    # *NOTES*
    # Wrap the `list_items` string in an unordered list (`<ul>`) and assign it to `response_data`.

    return HttpResponse(response_data)
    # *NOTES*
    # Return an `HttpResponse` with the `response_data` as the content.
    # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse

def monthly_challenge_by_number(request, month):
    # *NOTES*
    # This defines the `monthly_challenge_by_number` view function which handles requests to URLs with a numeric month.
    # The `month` parameter is an integer representing the month number.

    months = list(monthly_challenges.keys())
    # *NOTES*
    # Get a list of all month names from the `monthly_challenges` dictionary keys.

    if month > len(months):
        # *NOTES*
        # Check if the `month` parameter is greater than the number of months in the list.
        
        return HttpResponseNotFound("Invalid month")
        # *NOTES*
        # If the month number is invalid, return an `HttpResponseNotFound` with the message "Invalid month".
        # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseNotFound

    redirect_month = months[month - 1]
    # *NOTES*
    # Get the month name corresponding to the month number.
    # Subtract 1 from the month number to get the correct index in the list (since list indices start at 0).

    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    # *NOTES*
    # Use the `reverse` function to get the URL path for the `month-challenge` view.
    # The `args` parameter specifies the month name to pass to the URL pattern.
    # https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.reverse

    return HttpResponseRedirect(redirect_path)
    # *NOTES*
    # Return an `HttpResponseRedirect` to the `redirect_path`.
    # This will redirect the user to the URL for the month challenge.
    # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseRedirect

def monthly_challenge(request, month):
    # *NOTES*
    # This defines the `monthly_challenge` view function which handles requests to URLs with a string month.
    # The `month` parameter is a string representing the month name.

    try:
        challenge_text = monthly_challenges[month]
        # *NOTES*
        # Try to get the challenge text for the given month from the `monthly_challenges` dictionary.

        response_data = f"<h1>{challenge_text}</h1>"
        # *NOTES*
        # Wrap the `challenge_text` in an `<h1>` tag and assign it to `response_data`.

        return HttpResponse(response_data)
        # *NOTES*
        # Return an `HttpResponse` with the `response_data` as the content.
        # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse

    except KeyError:
        # *NOTES*
        # Catch a `KeyError` exception if the month is not found in the `monthly_challenges` dictionary.

        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
        # *NOTES*
        # Return an `HttpResponseNotFound` with the message "This month is not supported!".
        # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseNotFound
