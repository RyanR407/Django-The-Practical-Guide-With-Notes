from django.db import models

from django.core.validators import MinLengthValidator
# *NOTES*
# This line imports the `MinLengthValidator` from `django.core.validators`.
# `MinLengthValidator` is used to validate that a field has a minimum length.
# https://docs.djangoproject.com/en/5.0/ref/validators/#minlengthvalidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    email_address = models.EmailField()
    # *NOTES*
    # This line defines an `email_address` field in the `Author` model, which is an email field.
    # `EmailField` is used to store email addresses and validate their format.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#emailfield

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Post(models.Model):
    title = models.CharField(max_length=150)

    excerpt = models.CharField(max_length=200)

    image_name = models.CharField(max_length=100)

    date = models.DateField(auto_now=True)
    # *NOTES*
    # This line defines a `date` field in the `Post` model, which is a date field.
    # The `auto_now` argument automatically sets the field to the current date every time the object is saved.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#datefield

    slug = models.SlugField(unique=True, db_index=True)
    # *NOTES*
    # This line defines a `slug` field in the `Post` model, which is a slug field.
    # The `unique=True` argument ensures that each slug is unique.
    # The `db_index=True` argument creates a database index on this field for faster lookups.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#slugfield

    content = models.TextField(validators=[MinLengthValidator(10)])

    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    # *NOTES*
    # This line defines an `author` field in the `Post` model, which is a foreign key to the `Author` model.
    # The `on_delete=models.SET_NULL` argument sets the field to NULL if the referenced `Author` is deleted.
    # The `null=True` argument allows the field to be empty.
    # The `related_name="posts"` argument sets the name of the reverse relation from `Author` to `Post`.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#foreignkey

    tags = models.ManyToManyField(Tag)
    # *NOTES*
    # This line defines a `tags` field in the `Post` model, which is a many-to-many relationship with the `Tag` model.
    # This allows a post to have multiple tags and a tag to be associated with multiple posts.
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#manytomanyfield

    def __str__(self):
        return self.title