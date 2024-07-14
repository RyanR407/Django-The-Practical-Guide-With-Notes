from django.apps import AppConfig
# *NOTES*
# This line imports the `AppConfig` class from the `django.apps` module.
# `AppConfig` is used for configuring a Django application.
# https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig

class ChallengesConfig(AppConfig):
    # *NOTES*
    # This defines a new class named `ChallengesConfig` that inherits from `AppConfig`.
    # This class is used to configure the `challenges` application.
    # https://docs.djangoproject.com/en/5.0/ref/applications/#for-application-authors

    name = 'challenges'
    # *NOTES*
    # This attribute specifies the name of the application.
    # The name should match the directory name of the application.
    # https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.name
