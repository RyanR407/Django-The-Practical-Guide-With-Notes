"""
WSGI config for monthly_challenges project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
# *NOTES*
# This is a module-level docstring describing the purpose of this file.
# WSGI (Web Server Gateway Interface) is a standard interface between web server software and web applications written in Python.
# The docstring also provides a link to the Django documentation for more information on WSGI deployment.
# https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/

import os
# *NOTES*
# This line imports the `os` module, which provides a way of using operating system-dependent functionality.
# https://docs.python.org/3/library/os.html

from django.core.wsgi import get_wsgi_application
# *NOTES*
# This line imports the `get_wsgi_application` function from `django.core.wsgi`.
# The `get_wsgi_application` function returns a WSGI callable.
# https://docs.djangoproject.com/en/5.0/ref/wsgi/#django.core.wsgi.get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monthly_challenges.settings')
# *NOTES*
# This sets the `DJANGO_SETTINGS_MODULE` environment variable to point to the project's settings module.
# The `os.environ.setdefault` function sets an environment variable if it is not already set.
# https://docs.djangoproject.com/en/5.0/topics/settings/#designating-the-settings

application = get_wsgi_application()
# *NOTES*
# This calls the `get_wsgi_application` function to get the WSGI application callable and assigns it to the `application` variable.
# This `application` variable is then used by WSGI servers to communicate with the Django application.
# https://docs.djangoproject.com/en/5.0/ref/wsgi/#django.core.wsgi.get_wsgi_application
