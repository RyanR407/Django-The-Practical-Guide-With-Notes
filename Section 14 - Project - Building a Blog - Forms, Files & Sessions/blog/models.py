from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption
# *NOTES*
# This class defines the `Tag` model with a single field `caption`.
# The `__str__` method returns the caption of the tag.
# https://docs.djangoproject.com/en/5.0/ref/models/fields/

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
# *NOTES*
# This class defines the `Author` model with fields `first_name`, `last_name`, and `email_address`.
# The `full_name` method returns the full name of the author.
# The `__str__` method returns the full name of the author.
# https://docs.djangoproject.com/en/5.0/ref/models/fields/

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
# *NOTES*
# This class defines the `Post` model with various fields including `title`, `excerpt`, `image`, `date`, `slug`, `content`, `author`, and `tags`.
# The `author` field is a foreign key to the `Author` model and uses a `related_name` of `posts`.
# The `tags` field is a many-to-many relationship with the `Tag` model.
# The `__str__` method returns the title of the post.
# https://docs.djangoproject.com/en/5.0/ref/models/fields/

class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField() 
    text = models.TextField(max_length=400)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
# *NOTES*
# This class defines the `Comment` model with fields `user_name`, `user_email`, `text`, and `post`.
# The `post` field is a foreign key to the `Post` model and uses a `related_name` of `comments`.
# https://docs.djangoproject.com/en/5.0/ref/models/fields/
