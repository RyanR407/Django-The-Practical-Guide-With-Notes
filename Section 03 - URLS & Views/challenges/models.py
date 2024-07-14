from django.db import models
# *NOTES*
# This line imports the `models` module from `django.db`.
# The `models` module contains classes and functions for defining and interacting with database models in Django.
# https://docs.djangoproject.com/en/5.0/topics/db/models/

# Create your models here.
# *NOTES*
# This is a placeholder comment suggesting where to define models for the `challenges` application.
# Models are Python classes that represent database tables. Each model class corresponds to a table, and each attribute of the model class corresponds to a column in the table.
# https://docs.djangoproject.com/en/5.0/topics/db/models/#defining-models

# Example of a simple model:
class Challenge(models.Model):
    # *NOTES*
    # This defines a new model class named `Challenge` that inherits from `models.Model`.
    # The class will represent a table in the database.
    # https://docs.djangoproject.com/en/5.0/topics/db/models/#defining-models

    title = models.CharField(max_length=100)
    # *NOTES*
    # This defines a `title` field for the `Challenge` model.
    # The `models.CharField` class is used for string fields with a maximum length.
    # The `max_length` argument specifies the maximum length of the field.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.CharField

    description = models.TextField()
    # *NOTES*
    # This defines a `description` field for the `Challenge` model.
    # The `models.TextField` class is used for large text fields.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.TextField

    def __str__(self):
        # *NOTES*
        # This defines the `__str__` method for the `Challenge` model.
        # The `__str__` method returns a string representation of the model instance.
        # This is useful for displaying model instances in the Django admin or in the shell.
        # https://docs.djangoproject.com/en/5.0/ref/models/instances/#str

        return self.title
        # *NOTES*
        # This returns the `title` field as the string representation of the `Challenge` model instance.
        # This means that when a `Challenge` instance is printed, its `title` will be displayed.
        # https://docs.djangoproject.com/en/5.0/ref/models/instances/#str
