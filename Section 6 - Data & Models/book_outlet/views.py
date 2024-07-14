from django.shortcuts import get_object_or_404, render
# *NOTES*
# This line imports the `get_object_or_404` and `render` functions from `django.shortcuts`.
# `get_object_or_404` is used to retrieve an object or raise a 404 error if the object does not exist.
# `render` is used to render a template with a context and return an HttpResponse.
# https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#get-object-or-404
# https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render

from django.http import Http404
# *NOTES*
# This line imports the `Http404` exception class from `django.http`.
# `Http404` is used to raise a 404 not found error.
# https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.Http404

from django.db.models import Avg
# *NOTES*
# This line imports the `Avg` aggregate function from `django.db.models`.
# `Avg` is used to calculate the average value of a given field.
# https://docs.djangoproject.com/en/5.0/ref/models/querysets/#avg

from .models import Book
# *NOTES*
# This line imports the `Book` model from the current app's `models` module.
# The `Book` model represents the books in the database.
# https://docs.djangoproject.com/en/5.0/topics/db/models/

# Create your views here.

def index(request):
  books = Book.objects.all().order_by("-rating")
  # *NOTES*
  # This line retrieves all `Book` objects from the database and orders them by the `rating` field in descending order.
  # The `all()` method returns a QuerySet of all objects in the database.
  # The `order_by` method is used to sort the QuerySet.
  # https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.all
  # https://docs.djangoproject.com/en/5.0/ref/models/querysets/#order-by

  num_books = books.count()
  # *NOTES*
  # This line counts the total number of books in the QuerySet.
  # The `count()` method returns the number of objects in the QuerySet.
  # https://docs.djangoproject.com/en/5.0/ref/models/querysets/#count

  avg_rating = books.aggregate(Avg("rating")) # rating__avg, rating__min
  # *NOTES*
  # This line calculates the average rating of the books in the QuerySet.
  # The `aggregate` method is used to perform an aggregation (in this case, calculating the average rating).
  # The result is a dictionary with the average rating accessible via the key `rating__avg`.
  # https://docs.djangoproject.com/en/5.0/topics/db/aggregation/

  return render(request, "book_outlet/index.html", {
    "books": books,
    "total_number_of_books": num_books,
    "average_rating": avg_rating
  })
  # *NOTES*
  # This line renders the `index.html` template with the context containing the books, total number of books, and average rating.
  # The `render` function takes the request, template name, and context as arguments and returns an HttpResponse.
  # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render

def book_detail(request, slug):
  # *NOTES*
  # This line defines the `book_detail` view function, which handles requests to the book detail page.
  # The `request` parameter is an HttpRequest object representing the current request.
  # The `slug` parameter is a string representing the book's slug.

  # try:
  #   book = Book.objects.get(pk=id)
  # except:
  #   raise Http404()
  # *NOTES*
  # This commented-out code block attempts to retrieve a `Book` object by its primary key (`id`).
  # If the book is not found, it raises an `Http404` exception.

  book = get_object_or_404(Book, slug=slug)
  # *NOTES*
  # This line retrieves a `Book` object by its `slug` field using the `get_object_or_404` function.
  # If the book is not found, it raises an `Http404` exception.
  # This line is used to replace the commented out block of code above this line.
  # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#get-object-or-404

  return render(request, "book_outlet/book_detail.html", {
    "title": book.title,
    "author": book.author,
    "rating": book.rating,
    "is_bestseller": book.is_bestselling
  })
  # *NOTES*
  # This line renders the `book_detail.html` template with the context containing the book's title, author, rating, and bestseller status.
  # The `render` function takes the request, template name, and context as arguments and returns an HttpResponse.
  # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render
