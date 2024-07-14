"""monthly_challenges URL Configuration

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
# *NOTES*
# This is a module-level docstring describing the purpose of this file.
# It includes examples of how to add URLs for function views, class-based views, and including other URL configurations.
# https://docs.djangoproject.com/en/5.0/topics/http/urls/

from django.contrib import admin
# *NOTES*
# This line imports the `admin` module from `django.contrib`.
# The `admin` module is used to include the Django admin site.
# https://docs.djangoproject.com/en/5.0/ref/contrib/admin/

from django.urls import path, include
# *NOTES*
# This line imports the `path` and `include` functions from `django.urls`.
# The `path` function is used to define URL patterns.
# The `include` function is used to include other URL configurations.
# https://docs.djangoproject.com/en/5.0/ref/urls/#path
# https://docs.djangoproject.com/en/5.0/ref/urls/#include

urlpatterns = [
    # *NOTES*
    # The `urlpatterns` list routes URLs to views.
    # Each entry in the list is a call to the `path` function.
    # https://docs.djangoproject.com/en/5.0/topics/http/urls/#urlpatterns

    path('admin/', admin.site.urls),
    # *NOTES*
    # This URL pattern routes URLs starting with `admin/` to the Django admin site.
    # https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#reversing-admin-urls

    path("challenges/", include("challenges.urls"))
    # *NOTES*
    # This URL pattern routes URLs starting with `challenges/` to the URL patterns defined in the `challenges.urls` module.
    # The `include` function allows referencing other URL configurations.
    # https://docs.djangoproject.com/en/5.0/ref/urls/#include
]
