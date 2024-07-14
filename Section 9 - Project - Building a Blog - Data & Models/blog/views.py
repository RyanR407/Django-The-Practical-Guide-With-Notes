from django.shortcuts import render, get_object_or_404
# *NOTES*
# This line imports the `render` and `get_object_or_404` functions from `django.shortcuts`.
# `render` is used to render a template with a context and return an HttpResponse.
# `get_object_or_404` is used to retrieve an object or raise a 404 error if the object does not exist.
# https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render
# https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#get-object-or-404

from .models import Post
# *NOTES*
# This line imports the `Post` model from the current app's `models` module.
# The `Post` model represents the blog posts in the database.
# https://docs.djangoproject.com/en/5.0/topics/db/models/

# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    # *NOTES*
    # This line retrieves the latest 3 `Post` objects from the database ordered by the `date` field in descending order.
    # The `all()` method returns a QuerySet of all objects in the database.
    # The `order_by` method is used to sort the QuerySet.
    # The slicing `[:3]` is used to get the first 3 objects.
    # https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.all
    # https://docs.djangoproject.com/en/5.0/ref/models/querysets/#order-by

    return render(request, "blog/index.html", {
      "posts": latest_posts
    })
    # *NOTES*
    # This line renders the `index.html` template with the context containing the latest posts.
    # The `render` function takes the request, template name, and context as arguments and returns an HttpResponse.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    # *NOTES*
    # This line retrieves all `Post` objects from the database ordered by the `date` field in descending order.
    # The `all()` method returns a QuerySet of all objects in the database.
    # The `order_by` method is used to sort the QuerySet.
    # https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.all
    # https://docs.djangoproject.com/en/5.0/ref/models/querysets/#order-by

    return render(request, "blog/all-posts.html", {
      "all_posts": all_posts
    })
    # *NOTES*
    # This line renders the `all-posts.html` template with the context containing all posts.
    # The `render` function takes the request, template name, and context as arguments and returns an HttpResponse.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    # *NOTES*
    # This line retrieves a `Post` object by its `slug` field using the `get_object_or_404` function.
    # If the post is not found, it raises an `Http404` exception.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#get-object-or-404

    return render(request, "blog/post-detail.html", {
      "post": identified_post,
      "post_tags": identified_post.tags.all()
    })
    # *NOTES*
    # This line renders the `post-detail.html` template with the context containing the identified post and its tags.
    # The `render` function takes the request, template name, and context as arguments and returns an HttpResponse.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render

