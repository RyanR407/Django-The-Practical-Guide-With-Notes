from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    # Harry Potter 1 => harry-potter-1
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    # *NOTES*
    # The `blank=True` argument allows this field to be optional in forms.
    # This means that the field is allowed to be empty when creating or updating a `Book` instance.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.SlugField

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    # def save(self, *args, **kwargs):
    #    self.slug = slugify(self.title)
    #    super().save(*args, **kwargs)
    # *NOTES*
    # Removed save() because the slug is automatically set is admin.py with:
    # "prepopulated_fields = {"slug": ("title",)}"

    def __str__(self):
        return f"{self.title} ({self.rating})"
