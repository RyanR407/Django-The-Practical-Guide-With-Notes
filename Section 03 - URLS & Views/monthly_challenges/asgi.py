"""
ASGI config for monthly_challenges project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
# *NOTES*
# This is a module-level docstring describing the purpose of this file.
# ASGI (Asynchronous Server Gateway Interface) is a standard for Python asynchronous web apps and servers to communicate with each other.
# The docstring also provides a link to the Django documentation for more information on ASGI deployment.
# https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/

import os
# *NOTES*
# This line imports the `os` module, which provides a way of using operating system-dependent functionality.
# https://docs.python.org/3/library/os.html

from django.core.asgi import get_asgi_application
# *NOTES*
# This line imports the `get_asgi_application` function from `django.core.asgi`.
# The `get_asgi_application` function returns an ASGI callable.
# https://docs.djangoproject.com/en/5.0/ref/asgi/#django.core.asgi.get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monthly_challenges.settings')
# *NOTES*
# This sets the `DJANGO_SETTINGS_MODULE` environment variable to point to the project's settings module.
# The `os.environ.setdefault` function sets an environment variable if it is not already set.
# https://docs.djangoproject.com/en/5.0/topics/settings/#designating-the-settings

application = get_asgi_application()
# *NOTES*
# This calls the `get_asgi_application` function to get the ASGI application callable and assigns it to the `application` variable.
# This `application` variable is then used by ASGI servers to communicate with the Django application.
# https://docs.djangoproject.com/en/5.0/ref/asgi/#django.core.asgi.get_asgi_application
