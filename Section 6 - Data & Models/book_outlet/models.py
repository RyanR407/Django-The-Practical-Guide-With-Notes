from django.core import validators
# *NOTES*
# This line imports the `validators` module from `django.core`.
# The `validators` module contains various built-in validators that can be used to validate model fields.
# https://docs.djangoproject.com/en/5.0/ref/validators/

from django.db import models
# *NOTES*
# This line imports the `models` module from `django.db`.
# The `models` module is used to define database models in Django.
# https://docs.djangoproject.com/en/5.0/ref/models/

from django.core.validators import MinValueValidator, MaxValueValidator
# *NOTES*
# This line imports the `MinValueValidator` and `MaxValueValidator` classes from `django.core.validators`.
# These validators are used to enforce minimum and maximum value constraints on model fields.
# https://docs.djangoproject.com/en/5.0/ref/validators/#minvaluevalidator
# https://docs.djangoproject.com/en/5.0/ref/validators/#maxvaluevalidator

from django.urls import reverse
# *NOTES*
# This line imports the `reverse` function from `django.urls`.
# The `reverse` function is used to reverse-resolve URL names into URL paths.
# https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#reverse

from django.utils.text import slugify
# *NOTES*
# This line imports the `slugify` function from `django.utils.text`.
# The `slugify` function is used to convert strings into slugs (URL-friendly representations).
# https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.text.slugify

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    # *NOTES*
    # This line defines a `title` field in the `Book` model, which is a character field with a maximum length of 50.
    # `CharField` is used for short to medium-length strings.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#charfield

    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    # *NOTES*
    # This line defines a `rating` field in the `Book` model, which is an integer field.
    # It uses `MinValueValidator` and `MaxValueValidator` to ensure the rating is between 1 and 5.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#integerfield

    author = models.CharField(null=True, max_length=100)
    # *NOTES*
    # This line defines an `author` field in the `Book` model, which is a character field with a maximum length of 100.
    # The `null=True` argument allows this field to be optional.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#charfield

    is_bestselling = models.BooleanField(default=False)
    # *NOTES*
    # This line defines an `is_bestselling` field in the `Book` model, which is a boolean field.
    # The `default=False` argument sets the default value to `False`.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#booleanfield

    slug = models.SlugField(default="", null=False, db_index=True)
    # *NOTES*
    # This line defines a `slug` field in the `Book` model, which is a slug field.
    # The `default=""` argument sets the default value to an empty string.
    # The `null=False` argument ensures this field cannot be null.
    # The `db_index=True` argument creates a database index on this field for faster lookups.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#slugfield

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    # *NOTES*
    # This method returns the absolute URL for the `Book` instance.
    # The `reverse` function is used to generate the URL for the `book-detail` view, using the book's slug as an argument.
    # https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#reverse

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    # *NOTES*
    # This method overrides the default `save` method.
    # Before saving the `Book` instance, it sets the `slug` field to a slugified version of the `title` field.
    # The `slugify` function converts the title to a slug.
    # The `super().save(*args, **kwargs)` call ensures the original save method is still called.
    # https://docs.djangoproject.com/en/5.0/ref/models/instances/#saving-objects

    def __str__(self):
        return f"{self.title} ({self.rating})"
    # *NOTES*
    # This method returns a string representation of the `Book` instance.
    # It returns the title and rating of the book.
    # https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.__str__
