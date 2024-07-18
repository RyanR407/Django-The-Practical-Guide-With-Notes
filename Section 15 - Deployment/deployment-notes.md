# Deployment Considerations

* Choosing a Database, we used SQLite in the project.
  * Is it enough? For small apps it is, but you may need something more robust.
  * We use SQLite and a different DB.
* Adjust Settings
  * Hosting Provider specific settings.
  * Disable development-only settings.
* Collecting Static Files
  * Static files (just like user uploads) are not serverd automatically.
  * We had to add code to serve the Media files, we will need to do something similar for our deployed site.
* Handling Static & Uploaded File Serving
  * Static files (just like user uploads) are not serverd automatically.
* Choose a Host & Deploy
  * There are multiple options to deploy a Django app.
  * Dive into the host-specific documents and examples.

# Which Database

* So far, we have used SQLite which has one db file and is already setup for Django.
  * It is good for development, but may not cut it for production.
  * For large applications, it is slow.
  * If you lose the file, the data is lost. Hosted databases have automatic backups usually.
* Do we use SQL or NoSQL?
  * Django's model system is built to use SQL.
  * There is NoSQL support, but we are going to use SQL for simplicity.
  * We also need to decide which type of SQL database to use.
    * We know about SQLite already.
    * MySQL and Postgres has servers that run them and they are more performant.
  * We use SQLite and Postgres in this Deployment section.

# Django & Web Servers

* Django is not a web server, it is a framework that makes it easy to build websites.
  * Django knows how to work with incoming requests and create responses.
  * Django does not listen for requests or handle anything a server does.
  * `python manage.py runserver` was used jsut as a development web server, it is not meant for a production website.
* The "wsgi.py" and "asgi.py" files are meant for being used with real web servers.
  * There are 2 files because Django can use ASGI or WSGI.
  * [https://docs.djangoproject.com/en/5.0/howto/deployment/](https://docs.djangoproject.com/en/5.0/howto/deployment/)
  * We use WSGI in this deployment.

# Serving Static Files

* Django does not serve static files automatically in production like it is does during development.
  * This is by design, because Django is inefficient and slow serving the files, especially over a web server.
* There are 3 ways to handle serving files, we go over all 3.
  * The worst option is to serve the files through Django.
  * A better option is to configure both processes to run on the same server, using a different processes. One process will serve the files, and Django will run on another process. This will be substantially better performancewise than serving them through Django.
  * The best option is to use one server for Django, and another server for the files, that is optimized for serving files.

# Choosing a Hosting provider

* There are a multitude of hosting providers for Django.
  * Digital Ocean is a good option and has great documentation for deploying Django.
* We are going to use AWS, the biggest cloud provider.
  * We use their free option, that is configurable, but you don't have to configure every option.

# Getting Started & Revisiting Settings

* Create an AWS account, it requires a credit card though.
* If you plan on using a hosting provider, look at the pricing.
* For new customers, we can use the free tier, which allows you to use some services for free, up to a certain point.
* To start we are going to use SQLite.
* We have to work on dealing with the static/uploaded files.
* We make changes to the "settings.py" file:
  * The `SECRET_KEY` must be secure, you can do this by using environment variables. Do not use a key that was public in any way.
  * `DEBUG = True` needs to be changed to `False`.
  * `ALLOWED_HOSTS` will be updated with the host information later.
  * We will keep the `DATABASES` the same for now until we stop using SQLite.
  * We go over the `STATIC` files settings in the next video.
  * Ensure the rest of your app is setup correctly.
* You can go over the [Django Settings Documentation](https://docs.djangoproject.com/en/5.0/ref/settings/) for more info.

# Collecting Static Files

* Static files are files that you use on your website unrelated to the Django code.
  * They are usually .js, .css and images.
* Django can collect all of the static files from all of your apps and condense them into one folder. This folder is then served by either Django or a static file host.
  * You don't need to collect the files in development, because `python manage.py runserver` automatically does it.
  * In production, you have to manually collect them.
* You need to add a location for all the static files to be collected using `STATIC_ROOT`.
  * We use: `STATIC_ROOT = BASE_DIR / "staticfiles"`
  * We already used `MEDIA_ROOT` when handling uploads, it uses the same concept.
  * We keep `STATIC_URL = "/static/"` and `MEDIA_URL = "/files/"` the same because it is the URL for serving the static/uploaded files.
  * Do not use the same folder for the static and media files. You can, but it is a security issue because other people can upload malicious code.
* To collect the static files run:  `python manage.py collectstatic`
  * This collects all of the static files, from all apps, into the "staticfiles" folder.
  * Do not edit these files, always edit the ones from the original location, then run `collestatic` again.

# Serving Static Files

* We are going to try out the first option to serve the static files, which is the worst option, and use Django to serve them.
* We do this by going into the main app's `urls.py` and adding the `static()` like we did for file uploads.
* We use: `static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)`

# A Note About Migrations

* Before deploying, you need to make sure a couple of things have been done.
* Make sure that you run all of your migrations:
  * `python manage.py makemigrations`
  * `python manage.py migrate`
* Before deploying, it is a good idea to make your super user, if you haven'y done so yet.
  * `python manage.py createsuperuser`
* * We are ready to deploy the application now that we setup serving static files and initialized the database.

# Locking in Dependencies

* We want to lock in the packages we use for the app.
  * Stop the app if it is running.
  * Run the command: `pip freeze > requirements.txt`
    * This saves all of the dependencies into `requirements.txt`.
* We create a virtual environment with: `python venv folder_name`
  * We run a shell using the virtual environment.
  * We run `pip install Django` and `pip install Pillow`.
  * We create the text file with: `pip freeze > requirements.txt`
* AWS will use this `requirements.txt` file to install the necessary dependencies when we dploy the application.

# More on Virtual Environments

* [https://docs.python.org/3/library/venv.html#creating-virtual-environments](https://docs.python.org/3/library/venv.html#creating-virtual-environments)
* In the linked article, scroll down a bit to see the commands for activating virtual environments on macOS / Linux and Windows.
* As shown in the lecture, the easiest way of activating is to let VS Code do it.

# Using Environment Variables

* We are going to setup `ALLOWED_HOSTS` to work with the server, using the domain.
  * Usually you will know the value in advance, since it is your website's domain, but often you don't.
* The best way to deal with information that is private, changes, or is not known before you deploy, is to use environment variables.
  * We use `getenv` to get environment variables.
  * `from os import getenv`
* We setup `ALLOWED_HOSTS` to use an environment variable:
  * `ALLOWED_HOSTS = [getenv("APP_HOST")]`
* It is also advisable to setup `SECRET_KEY` to use an environment variable:
  * `SECRET_KEY = [getenv("SECRET_KEY")]`
  * You should never keep your `SECRET_KEY` in code that you upload to a repo or code that you give out.
* For `DEBUG`, we want it to be `True` in develpoment and `False` in Production.
  * You can use something like this to witch based on the environment variable:
  * `DEBUG = getenv("IS_DEVELOPMENT", True)`
  * The second argument is the default value, we keep it `True` so we don't need to set it in development.

# Deploying with Elastic Beanstalk

* In the AWS Management Console, we use `Elastic Beanstalk`.
  * It is a service that makes deploying websites simple.
* Click `Create Application`.
* Fill out the form.
  * Enter an `Application name`.
  * For `Platform` choose Python and select the version closest to your version used in the app.
  * Select `Upload your code`.
* Before uploading, we have to prepare the code for Elastic Beanstalk.
  * Add the `.ebextensions` folder.
  * In the folder add a `django.config` file. The contents of the file are:

    ```
    option_settings:
      aws:elasticbeanstalk:container:python:
        WSGIPath: my_site.wsgi:application
    ```

    * `my_site` needs to be the project folder name that has the `wsgi.py` file in it.
  * We create a `code.zip` file with the following files/folders.

    * `.ebextensions` folder, `blog` folder, `db.sqlite3` file, `manage.py` file, `my_site` folder, `requirements.txt` file, `staticfiles` folder, `templates` folder, `uploads` folder.
* Upload the `code.zip` file to the Elastic Beanstalk form.
* Click on `Configure more options`.
* Pick the `Preset` you want, we use `Single instance (Free Teir eligible)`.
* Go to the `Software` section and click `Edit`.
* You can set your environment variables under the `Environment properties`.
  * Keep any that are there.
  * Add in the values for `IS_DEVELOPMENT` (which should be `False`), `APP_HOST`, `SECRET_KEY`, etc.
    * You won't know `APP_HOST` until you deploy, so put in a dummy value.
* Click `Save`.
* You can setup other options like a database, monitoring, notifications, etc. but we are not going to.
* The app is now ready to be deployed. Click `Create app`.
* It will take several minutes to deploy and you should see an "OK" message.
* We get an error because the `APP_HOST` isn't setup in the `ALLOWED_HOSTS`.
  * The error gives you the domain that you can add as the `APP_HOST` in the `Environment properties`. You do not need the `http://`, only the domain name.
  * click "Apply".
* The app should run now.

# SSL & Custom Domains

* Adding SSL and/or a Custom Domain costs money.
* To use SSL, you need to use a Load Balancer. Refer to the Docs.
  * [https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https.html](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https.html)
* For Custom Domains, you use the AWS service `Route 53`. Refer to the Docs.
  * [https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customdomains.html](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customdomains.html)

# Connecting PostgreSQL

# Serving Static Files Separately

# Serving Static Files via S3

# Moving File Uploads to S3
