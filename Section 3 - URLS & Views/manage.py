#!/usr/bin/env python
# *NOTES*
# This is a shebang line that tells the system to use the Python interpreter to run this script.
# https://docs.python.org/3/using/unix.html#shebang-line

"""Django's command-line utility for administrative tasks."""
# *NOTES*
# This is a module-level docstring that describes the purpose of the `manage.py` script.

import os
import sys
# *NOTES*
# These lines import the `os` and `sys` modules.
# The `os` module provides a way to use operating system-dependent functionality.
# The `sys` module provides access to some variables used or maintained by the Python interpreter.
# https://docs.python.org/3/library/os.html
# https://docs.python.org/3/library/sys.html

def main():
    """Run administrative tasks."""
    # *NOTES*
    # This defines the `main` function which handles administrative tasks.
    # The docstring describes the purpose of the function.

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monthly_challenges.settings')
    # *NOTES*
    # This sets the default Django settings module to 'monthly_challenges.settings'.
    # The `os.environ.setdefault` function sets an environment variable if it is not already set.
    # https://docs.djangoproject.com/en/5.0/ref/settings/#setting

    try:
        from django.core.management import execute_from_command_line
        # *NOTES*
        # This imports the `execute_from_command_line` function from `django.core.management`.
        # The `execute_from_command_line` function is used to run command-line utilities for Django.
        # https://docs.djangoproject.com/en/5.0/ref/django-admin/#django.core.management.execute_from_command_line

    except ImportError as exc:
        # *NOTES*
        # This catches an `ImportError` if the Django module cannot be imported.
        
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        # *NOTES*
        # This raises an `ImportError` with a custom error message if Django cannot be imported.
        # The error message suggests checking if Django is installed and available on the `PYTHONPATH`, and whether a virtual environment is activated.
        # https://docs.python.org/3/library/exceptions.html#ImportError

    execute_from_command_line(sys.argv)
    # *NOTES*
    # This calls the `execute_from_command_line` function with the command-line arguments.
    # This is what makes it possible to run Django management commands from the command line.
    # https://docs.djangoproject.com/en/5.0/ref/django-admin/#django.core.management.execute_from_command_line

if __name__ == '__main__':
    main()
    # *NOTES*
    # This checks if the script is being run directly (not imported as a module).
    # If so, it calls the `main` function to execute the script.
    # https://docs.python.org/3/library/__main__.html
