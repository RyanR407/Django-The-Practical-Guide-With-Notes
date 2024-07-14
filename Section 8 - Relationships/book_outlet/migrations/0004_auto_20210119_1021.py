# Generated by Django 3.1.5 on 2021-01-19 10:21

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0003_book_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        # *NOTES*
        # This operation creates a new model called `Author`.
        # The `Author` model has three fields: `id`, `first_name`, and `last_name`.
        # The `id` field is an automatically generated primary key.
        # The `first_name` and `last_name` fields are character fields with a maximum length of 100.
        # https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.AutoField
        # https://docs.djangoproject.com/en/5.0/ref/models/fields/#charfield

        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
        # *NOTES*
        # This operation modifies the `slug` field in the `Book` model.
        # The `blank=True` argument allows this field to be optional in forms.
        # The `default=''` argument sets the default value to an empty string.
        # https://docs.djangoproject.com/en/5.0/ref/models/fields/#slugfield

        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book_outlet.author'),
        ),
        # *NOTES*
        # This operation modifies the `author` field in the `Book` model.
        # The `author` field is now a foreign key to the `Author` model.
        # The `null=True` argument allows this field to be optional.
        # The `on_delete=django.db.models.deletion.CASCADE` argument specifies that when the referenced `Author` object is deleted, the `Book` object should also be deleted.
        # https://docs.djangoproject.com/en/5.0/ref/models/fields/#foreignkey
        # https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey.on_delete
    ]