from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, 
         name="post-detail-page")  # /posts/my-first-post
    # *NOTES*
    # This line defines a URL pattern that matches the URL path "posts/<slug:slug>".
    # The '<slug:slug>' part is a path converter that captures a slug and passes it to the view as the 'slug' keyword argument.
    # It uses the 'post_detail' view to handle the request.
    # The name "post-detail-page" allows referencing this URL pattern in templates and other code.
    # https://docs.djangoproject.com/en/5.0/topics/http/urls/#path-converters
    # https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.path

]
