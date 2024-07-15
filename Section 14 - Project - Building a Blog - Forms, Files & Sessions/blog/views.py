from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View

from .models import Post
from .forms import CommentForm

# Create your views here.

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"
    # *NOTES*
    # This class defines a `StartingPageView` that inherits from `ListView`.
    # The `template_name` attribute specifies the template to render (`blog/index.html`).
    # The `model` attribute specifies the model to use (`Post`).
    # The `ordering` attribute specifies the default ordering of the objects.
    # The `context_object_name` attribute specifies the name of the context variable to use for the list of objects (`posts`).
    # https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#listview

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
    # *NOTES*
    # This method overrides `get_queryset` to return the first three posts.
    # `get_queryset` is used to customize the queryset that the view will use.
    # https://docs.djangoproject.com/en/5.0/ref/class-based-views/mixins-list/#django.views.generic.list.MultipleObjectMixin.get_queryset

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"
# *NOTES*
# This class defines an `AllPostsView` that inherits from `ListView`.
# The `template_name` attribute specifies the template to render (`blog/all-posts.html`).
# The `model` attribute specifies the model to use (`Post`).
# The `ordering` attribute specifies the default ordering of the objects.
# The `context_object_name` attribute specifies the name of the context variable to use for the list of objects (`all_posts`).
# https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#listview

class SinglePostView(View):
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False

        return is_saved_for_later
    # *NOTES*
    # This method checks if a post is stored in the session.
    # It retrieves the `stored_posts` from the session and checks if `post_id` is in `stored_posts`.
    # https://docs.djangoproject.com/en/5.0/topics/http/sessions/

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)
    # *NOTES*
    # This method handles GET requests.
    # It retrieves the post by its slug and renders the `post-detail.html` template with the post's context.
    # https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#handling-get-requests

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)
# *NOTES*
# This method handles POST requests.
# It validates the comment form, saves the comment if valid, and redirects to the post detail page.
# If the form is not valid, it re-renders the `post-detail.html` template with the form errors.
# https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#handling-post-requests

class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "blog/stored-posts.html", context)
  # *NOTES*
  # This method handles GET requests.
  # It retrieves stored posts from the session and renders the `stored-posts.html` template with the posts.
  # If there are no stored posts, it sets the context to indicate that there are no posts.
  # https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#handling-get-requests

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts
        
        return HttpResponseRedirect("/")
  # *NOTES*
  # This method handles POST requests.
  # It adds or removes a post ID from the stored posts in the session based on whether it is already stored.
  # After updating the session, it redirects to the home page.
  # https://docs.djangoproject.com/en/5.0/topics/http/sessions/
  # https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseRedirect
