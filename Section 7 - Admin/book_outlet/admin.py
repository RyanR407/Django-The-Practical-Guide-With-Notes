from django.contrib import admin
# *NOTES*
# This line imports the `admin` module from `django.contrib`.
# The `admin` module is used to register models and customize the admin interface.
# https://docs.djangoproject.com/en/5.0/ref/contrib/admin/

from .models import Book
# *NOTES*
# This line imports the `Book` model from the current app's `models` module.
# The `Book` model will be registered with the admin interface.
# https://docs.djangoproject.com/en/5.0/ref/models/

# Register your models here.

class BookAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  # *NOTES*
  # This line sets the `prepopulated_fields` attribute for the `BookAdmin` class.
  # The `slug` field will be automatically populated based on the `title` field.
  # https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.prepopulated_fields

  list_filter = ("author", "rating",)
  # *NOTES*
  # This line sets the `list_filter` attribute for the `BookAdmin` class.
  # The admin interface will include filters for the `author` and `rating` fields.
  # https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter

  list_display = ("title", "author",)
  # *NOTES*
  # This line sets the `list_display` attribute for the `BookAdmin` class.
  # The admin interface will display the `title` and `author` fields in the list view.
  # https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display

admin.site.register(Book, BookAdmin)
# *NOTES*
# This line registers the `Book` model with the admin interface using the `BookAdmin` configuration.
# This makes the `Book` model available in the admin interface with the specified customizations.
# https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.site.register
