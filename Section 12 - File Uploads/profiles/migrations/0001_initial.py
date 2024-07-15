# Generated by Django 3.1.5 on 2021-01-26 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            # *NOTES*
            # This line creates a new model named `UserProfile`.
            # The `CreateModel` operation is used to define a new database table and its fields.
            # https://docs.djangoproject.com/en/3.1/ref/migration-operations/#createmodel
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                # *NOTES*
                # This line defines the `id` field for the `UserProfile` model.
                # `AutoField` is an integer field that automatically increments according to available IDs.
                # It is used as the primary key for the model.
                # https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.AutoField

                ('image', models.FileField(upload_to='images')),
                # *NOTES*
                # This line defines the `image` field for the `UserProfile` model.
                # `FileField` is used for uploading files.
                # The `upload_to` argument specifies the directory within `MEDIA_ROOT` where uploaded files will be stored.
                # https://docs.djangoproject.com/en/3.1/ref/models/fields/#filefield
            ],
        ),
    ]
