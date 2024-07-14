# Generated by Django 3.1.5 on 2021-01-19 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0006_auto_20210119_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('code', models.CharField(max_length=2)),
            ],
        ),
        # *NOTES*
        # This operation creates a new model called `Country`.
        # The `Country` model has three fields: `id`, `name`, and `code`.
        # The `id` field is an automatically generated primary key.
        # The `name` field is a character field with a maximum length of 80.
        # The `code` field is a character field with a maximum length of 2.
        # https://docs.djangoproject.com/en/5.0/ref/models/fields/#autofield
        # https://docs.djangoproject.com/en/5.0/ref/models/fields/#charfield

        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Address Entries'},
        ),
        # *NOTES*
        # This operation alters the model options for the `Address` model.
        # The `verbose_name_plural` option is set to "Address Entries".
        # This changes the plural name of the `Address` model in the admin interface.
        # https://docs.djangoproject.com/en/5.0/ref/models/options/#verbose-name-plural

        migrations.AddField(
            model_name='book',
            name='published_countries',
            field=models.ManyToManyField(to='book_outlet.Country'),
        ),
        # *NOTES*
        # This operation adds a `published_countries` field to the `Book` model.
        # The `published_countries` field is a many-to-many relationship to the `Country` model.
        # This allows a book to be associated with multiple countries and vice versa.
        # https://docs.djangoproject.com/en/5.0/ref/models/fields/#manytomanyfield
    ]
