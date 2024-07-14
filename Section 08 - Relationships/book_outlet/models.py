from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.query import FlatValuesListIterable
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)
    # *NOTES*
    # The `Country` model has two fields: `name` and `code`.
    # `name` is a CharField with a maximum length of 80, and `code` is a CharField with a maximum length of 2.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#charfield

    def __str__(self):
        return self.name
    # *NOTES*
    # The `__str__` method returns the name of the country.
    # This is used to provide a human-readable representation of the object.
    # https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.__str__

    class Meta:
        verbose_name_plural = "Countries"
    # *NOTES*
    # The `Meta` class inside the model defines additional options.
    # `verbose_name_plural` is used to specify the plural name for the model.
    # https://docs.djangoproject.com/en/5.0/ref/models/options/#verbose-name-plural

class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    # *NOTES*
    # The `Address` model has three fields: `street`, `postal_code`, and `city`.
    # All three fields are CharFields with specified maximum lengths.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#charfield

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"
    # *NOTES*
    # The `__str__` method returns a formatted string representing the address.
    # This is used to provide a human-readable representation of the object.
    # https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.__str__

    class Meta:
        verbose_name_plural = "Address Entries"
    # *NOTES*
    # The `Meta` class inside the model defines additional options.
    # `verbose_name_plural` is used to specify the plural name for the model.
    # https://docs.djangoproject.com/en/5.0/ref/models/options/#verbose-name-plural

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True)
    # *NOTES*
    # The `Author` model has three fields: `first_name`, `last_name`, and `address`.
    # `first_name` and `last_name` are CharFields with a maximum length of 100.
    # `address` is a OneToOneField related to the `Address` model, with `on_delete` set to `CASCADE` and allowing null values.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#onetoonefield

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    # *NOTES*
    # The `full_name` method returns the full name of the author by combining the first name and last name.
    # https://docs.djangoproject.com/en/5.0/ref/models/instances/#custom-methods

    def __str__(self):
        return self.full_name()
    # *NOTES*
    # The `__str__` method returns the full name of the author.
    # This is used to provide a human-readable representation of the object.
    # https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.__str__

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    # Harry Potter 1 => harry-potter-1
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    # *NOTES*
    # The `blank=True` argument allows this field to be optional in forms.
    # This means that the field is allowed to be empty when creating or updating a `Book` instance.
    # The `db_index=True` argument creates a database index on this field for faster lookups.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.SlugField

    published_countries = models.ManyToManyField(Country, null=False)
    # *NOTES*
    # The `published_countries` field is a ManyToManyField related to the `Country` model.
    # This allows a book to be published in multiple countries.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#manytomanyfield

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    # *NOTES*
    # This method returns the absolute URL for the `Book` instance.
    # The `reverse` function is used to generate the URL for the `book-detail` view, using the book's slug as an argument.
    # https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#reverse

    def __str__(self):
        return f"{self.title} ({self.rating})"
    # *NOTES*
    # This method returns a string representation of the `Book` instance.
    # It returns the title and rating of the book.
    # https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.__str__
