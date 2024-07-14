from django.contrib import admin
# *NOTES*
# This line imports the `admin` module from `django.contrib`.
# The `admin` module is used to register models and customize the admin interface.
# https://docs.djangoproject.com/en/5.0/ref/contrib/admin/

from .models import Post, Author, Tag
# *NOTES*
# This line imports the `Post`, `Author`, and `Tag` models from the current app's `models` module.
# These models will be registered with the admin interface.
# https://docs.djangoproject.com/en/5.0/ref/models/

# Register your models here

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    # *NOTES*
    # This line sets the `list_filter` attribute for the `PostAdmin` class.
    # The admin interface will include filters for the `author`, `tags`, and `date` fields.
    # https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter

    list_display = ("title", "date", "author",)
    # *NOTES*
    # This line sets the `list_display` attribute for the `PostAdmin` class.
    # The admin interface will display the `title`, `date`, and `author` fields in the list view.
    # https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display

    prepopulated_fields = {"slug": ("title",)}
    # *NOTES*
    # This line sets the `prepopulated_fields` attribute for the `PostAdmin` class.
    # The `slug` field will be automatically populated based on the `title` field.
    # https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.prepopulated_fields


admin.site.register(Post, PostAdmin)
# *NOTES*
# This line registers the `Post` model with the admin interface using the `PostAdmin` configuration.
# This makes the `Post` model available in the admin interface with the specified customizations.
# https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.site.register

admin.site.register(Author)
# *NOTES*
# This line registers the `Author` model with the admin interface.
# This makes the `Author` model available in the admin interface with the default configuration.
# https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.site.register

admin.site.register(Tag)
# *NOTES*
# This line registers the `Tag` model with the admin interface.
# This makes the `Tag` model available in the admin interface with the default configuration.
# https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.site.register
