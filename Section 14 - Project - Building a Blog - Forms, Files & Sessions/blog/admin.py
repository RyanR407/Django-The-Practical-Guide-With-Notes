from django.contrib import admin

from .models import Post, Author, Tag, Comment

# Register your models here

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}
    # *NOTES*
    # `PostAdmin` is a custom admin class for the `Post` model.
    # `list_filter` adds filters in the admin sidebar for `author`, `tags`, and `date`.
    # `list_display` specifies the fields to display in the list view of the admin.
    # `prepopulated_fields` populates the `slug` field automatically based on the `title`.
    # https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#modeladmin-options

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")
    # *NOTES*
    # `CommentAdmin` is a custom admin class for the `Comment` model.
    # `list_display` specifies the fields to display in the list view of the admin.
    # https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#modeladmin-options

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
# *NOTES*
# This registers the `Post`, `Author`, `Tag`, and `Comment` models with the admin site.
# `Post` and `Comment` use custom admin classes `PostAdmin` and `CommentAdmin`, respectively.
# https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#registering-models
