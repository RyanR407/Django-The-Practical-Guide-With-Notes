from django.contrib import admin

from .models import Book, Author, Address, Country

# Register your models here.

class BookAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_filter = ("author", "rating",)
  list_display = ("title", "author",)

admin.site.register(Book, BookAdmin)
# *NOTES*
# This line registers the `Book` model with the admin interface using the `BookAdmin` configuration.
# This makes the `Book` model available in the admin interface with the specified customizations.
# https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.site.register

admin.site.register(Author)
# *NOTES*
# This line registers the `Author` model with the admin interface.
# This makes the `Author` model available in the admin interface without any additional customizations.
# https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.site.register

admin.site.register(Address)
# *NOTES*
# This line registers the `Address` model with the admin interface.
# This makes the `Address` model available in the admin interface without any additional customizations.
# https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.site.register

admin.site.register(Country)
# *NOTES*
# This line registers the `Country` model with the admin interface.
# This makes the `Country` model available in the admin interface without any additional customizations.
# https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.site.register
