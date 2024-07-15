from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(),
         name="post-detail-page"),  # /posts/my-first-post
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]
# *NOTES*
# This URL configuration maps URLs to views.
# The `path` function is used to define URL patterns and associate them with views.
# `as_view()` is used to convert class-based views into callable view functions.
# https://docs.djangoproject.com/en/5.0/topics/http/urls/