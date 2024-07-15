"""feedback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("reviews.urls")),
    path("profiles/", include("profiles.urls"))
    # *NOTES*
    # This line adds a URL pattern that includes the URLs from the `profiles` app.
    # Requests to URLs starting with "profiles/" will be routed to `profiles.urls`.
    # https://docs.djangoproject.com/en/3.1/topics/http/urls/#including-other-urlconfs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# *NOTES*
# This line adds a URL pattern for serving media files during development.
# `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` uses the `MEDIA_URL` and `MEDIA_ROOT` settings to serve media files.
# This is only suitable for development and should not be used in production.
# https://docs.djangoproject.com/en/3.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development
