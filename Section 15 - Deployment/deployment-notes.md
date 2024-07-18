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
* Resources:
  * [https://docs.djangoproject.com/en/5.0/ref/databases/](https://docs.djangoproject.com/en/5.0/ref/databases/)
  * [https://docs.djangoproject.com/en/5.0/ref/databases/#postgresql-notes](https://docs.djangoproject.com/en/5.0/ref/databases/#postgresql-notes)
  * [https://docs.aws.amazon.com/rds/index.html](https://docs.aws.amazon.com/rds/index.html)

# Django & Web Servers

* Django is not a web server, it is a framework that makes it easy to build websites.
  * Django knows how to work with incoming requests and create responses.
  * Django does not listen for requests or handle anything a server does.
  * `python manage.py runserver` was used jsut as a development web server, it is not meant for a production website.
* The "wsgi.py" and "asgi.py" files are meant for being used with real web servers.
  * There are 2 files because Django can use ASGI or WSGI.
  * [https://docs.djangoproject.com/en/5.0/howto/deployment/](https://docs.djangoproject.com/en/5.0/howto/deployment/)
  * We use WSGI in this deployment.
* Resources:
* [https://docs.djangoproject.com/en/5.0/howto/deployment/](https://docs.djangoproject.com/en/5.0/howto/deployment/)
* [https://uwsgi-docs.readthedocs.io/en/latest/](https://uwsgi-docs.readthedocs.io/en/latest/)

# Serving Static Files

* Django does not serve static files automatically in production like it is does during development.
  * This is by design, because Django is inefficient and slow serving the files, especially over a web server.
* There are 3 ways to handle serving files, we go over all 3.
  * The worst option is to serve the files through Django.
  * A better option is to configure both processes to run on the same server, using a different processes. One process will serve the files, and Django will run on another process. This will be substantially better performancewise than serving them through Django.
  * The best option is to use one server for Django, and another server for the files, that is optimized for serving files.
* Resources:
  * [https://docs.djangoproject.com/en/5.0/howto/static-files/](https://docs.djangoproject.com/en/5.0/howto/static-files/)
  * [https://docs.aws.amazon.com/s3/index.html](https://docs.aws.amazon.com/s3/index.html)
  * [https://realpython.com/django-nginx-gunicorn/](https://realpython.com/django-nginx-gunicorn/)

# Choosing a Hosting provider

* There are a multitude of hosting providers for Django.
  * Digital Ocean is a good option and has great documentation for deploying Django.
* We are going to use AWS, the biggest cloud provider.
  * We use their free option, that is configurable, but you don't have to configure every option.
* Resources:
  * [https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)
  * [https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu)
  * [https://www.digitalocean.com/community/tutorials/how-to-deploy-django-to-app-platform](https://www.digitalocean.com/community/tutorials/how-to-deploy-django-to-app-platform)

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
* Resources:
  * [Django Settings Documentation](https://docs.djangoproject.com/en/5.0/ref/settings/)
  * [https://aws.amazon.com/pricing/](https://aws.amazon.com/pricing/)

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
* Resources:
  * [https://docs.djangoproject.com/en/5.0/ref/django-admin/#collectstatic](https://docs.djangoproject.com/en/5.0/ref/django-admin/#collectstatic)

# Serving Static Files

* We are going to try out the first option to serve the static files, which is the worst option, and use Django to serve them.
* We do this by going into the main app's `urls.py` and adding the `static()` like we did for file uploads.
* We use: `static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)`
* Resources:
  * [https://docs.djangoproject.com/en/5.0/howto/static-files/#serving-static-files-during-development](https://docs.djangoproject.com/en/5.0/howto/static-files/#serving-static-files-during-development)

# A Note About Migrations

* Before deploying, you need to make sure a couple of things have been done.
* Make sure that you run all of your migrations:
  * `python manage.py makemigrations`
  * `python manage.py migrate`
* Before deploying, it is a good idea to make your super user, if you haven'y done so yet.
  * `python manage.py createsuperuser`
* We are ready to deploy the application now that we setup serving static files and initialized the database.
* Resources:
  * [https://docs.djangoproject.com/en/5.0/topics/migrations/](https://docs.djangoproject.com/en/5.0/topics/migrations/)

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
* Resources:
  * [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)
  * [https://pip.pypa.io/en/stable/cli/pip_freeze/](https://pip.pypa.io/en/stable/cli/pip_freeze/)

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
* Resources:
  * [https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/#use-environment-variables-for-secrets](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/#use-environment-variables-for-secrets)

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
* Resources:
  * [https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html)
  * [https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html)

# SSL & Custom Domains

* Adding SSL and/or a Custom Domain costs money.
* To use SSL, you need to use a Load Balancer. Refer to the Docs.
  * [https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https.html](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https.html)
* For Custom Domains, you use the AWS service `Route 53`. Refer to the Docs.
  * [https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customdomains.html](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customdomains.html)
* Other Resources:
  * [https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)

# Connecting PostgreSQL

* We have been using SQLite up to this point, but the Django ORM also supports MySQL and Postgres.
* [https://docs.djangoproject.com/en/5.0/ref/databases/#postgresql-notes](https://docs.djangoproject.com/en/5.0/ref/databases/#postgresql-notes)
* We need to install `psychopg2`, stop the server and run this ommand in the virtual environment: `pip install psocopg2`
* Update the `requirements.txt` file:  `pip freeze > requirements.txt`
* In AWS, we are going to use the `RDS` service for the Postgres database.
  * Click `Create database`
  * Select `PostgreSQL` and pick the version you want to use.
  * Under "Templates" select `Free tier`, otherwise you will have to pay.
  * Give the database and identifier, we use `django-blog`.
  * Create the `Master username` and `Master password`, which is used for accessing the database.
  * `Disable storage autoscaling` so it does not charge money if the database runs out of room.
  * Change `Public access` to `Yes`.
  * For "VPC security group" we `Create new`, we name it `django-db`.
  * There are a ton of options to customize, and you will want to when in Production, but for our purposes, this setup is good to go.
  * Click `Create database`.
* In settings.py, we need to setup the Django app to use Postgres:
  * We change `DATABASES` to:
    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': getenv("DB_USER"),
            'PASSWORD': getenv("DB_PASSWORD"),
            'HOST': getenv("DB_HOST"),
            'PORT': '5432'
        }
    }
    ```
    * The information for filling this out comes from the AWS RDS PostgreSQL instance, on the `View credential details` pop-up.
    * It is advised to use environment variables so I changed it to use them.
* The database is now setup, so we want to prepare it like we did before for SQLite, before we upload the updated code.
  * `python manage.py makemigrations`
  * `python manage.py migrate`
  * `python manage.py createsuperuser`
* We try to run the code locally, so we can test if the database connection works.
  * There is an error because `localhost` is not in `ALLOWED_HOSTS`.
  * We update it to:  `ALLOWED_HOSTS = [getend("APP_HOST", "localhost")]`
  * After this, the blog runs fine, we login to Admin, and the quit the app.
* We create a `code.zip` file with the following files/folders.
  * `.ebextensions` folder, `blog` folder, `manage.py` file, `my_site` folder, `requirements.txt` file, `staticfiles` folder, `templates` folder, `uploads` folder
* We go back to the `Elastic Beanstalk` console.
  * Go to the application by clicking on the name under the `Applications` tab.
  * Click on `Update and deploy`.
  * Upload the `code.zip` file.
  * Click `Deploy`.
* Go to the `RDS` console.
  * Click on the `Connectivity & Security` tab in the center
  * Look at the `VPC security groups`, which is a firewall for this service.
  * The default setting only allows local traffic.
  * Click on the `Inbound rules` tab in the center.
  * Click on `Edit inbound rules`.
  * Change the `Source` to `Anywhere`.
  * Click `Save rules` at the bottom.
* The website will now work with the database.
* Resources:
  * [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html)
  * [https://www.psycopg.org/docs/](https://www.psycopg.org/docs/)

# Serving Static Files Separately

* Currently, we are having Django serve the static files.
* We are going to make it so the same service serves the files and runs Django, but in different processes.
* Nginx is used as the server, which can be seen in the Elastic Beanstalk Configuration.
* We can tell the server how to serve static files and that we want them served separately.
* In the `.ebextensions` folder, add the file `static-files.config` with this code:
  ```
  option_settings:
  aws:elasticbeanstalk:environment:proxy:staticfiles:
    /static: staticfiles
    /files: uploads
  ```
  * The `/static` and `/files` are the `STATIC_URL` and `MEDIA_URL` respectively.
  * The `staticfiles` and `uploads` are the `STATIC_ROOT` and `MEDIA_ROOT` respectively.
* In the main app's `urls.py`, remove the `static()` lines for the media and static files.
* We create a `code.zip` file with the following files/folders.
  * `.ebextensions` folder, `blog` folder, `manage.py` file, `my_site` folder, `requirements.txt` file, `staticfiles` folder, `templates` folder, `uploads` folder
* We go back to the `Elastic Beanstalk` console.
  * Go to the application by clicking on the name under the `Applications` tab.
  * Click on `Update and deploy`.
  * Upload the `code.zip` file.
  * Click `Deploy`.
* The server will now serve Django and the static files separately.
* We go into the Admin page and test uploading, by creating a new Post and uploading a picture.
* We add a test comment, to see if it works.
* Resources:
  * [https://dev.to/koladev/serving-djangos-static-files-with-nginx-3nc4](https://dev.to/koladev/serving-djangos-static-files-with-nginx-3nc4)
  * [https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions.html](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions.html)

# Serving Static Files via S3

* Currently, we are using the same service to serve the files and run Django, but in different processes.
* We are going to make it so that the static files and any files we upload are served from a server that is optimized for serving files.
* We use `S3` for doing this, so go into the `S3` console on AWS.
* To store the files we click `Create bucket` which is essentially creating a folder.
  * The name has to be globally unique.
  * Un-check the `Black all public access` because we want it publicly accessible.
  * Click `Create bucket`.
* Inside of the bucket, go to the `Properties` tab.
  * Under `Static website hosting` click `Edit`.
  * Change `Static website hosting` to `Enable`. We aren't actually hosting a website, but we are giving it static assets.
  * Set `Index document` to `index.html`.
  * Set `Error document` to `error.html`.
  * Click `Save changes`.
* Go to the `Premissions` tab.
  * Click `Edit` in the `Cross-origina resource sharing (CORS)` section.
  * Paste this in:
    ```
    [{"AllowedHeaders": ["*"], "AllowedMEthods": ["GET"],"AllowedOrigins": ["*"],"ExposeHeaders": []}]
    ```
    * This will ensure that the files can be reached by the Django service.
  * Click `Save changes`.
* Stay in the `Premissions` tab.
  * Go to `Bucket policy` and click `Edit`.
  * Use this policy:
    ```
    {"Version":"2012-10-17", "Statement: [{"Sid": "PublicReadGetObject", "Effect": "Allow", "Principal": "*", "Action": ["s3:GetObject"], "Resource": ["arn:aws:s3:::example-bucket/*"]}]}
    ```
  * Change `example-bucket` to your bucket's name.
  * Click `Save changes`.
* In order to be able to upload files, we need to grant our Django app write access.
* Go to the `IAM` console on AWS.
* Go to `Groups`. We create a group that has S3 access only.
  * `Create New Group`.
  * Give it a name.
  * Give it minimum access by selecting `AmnazonS3FullAccess`.
  * Click `Next Step`
  * Click `Create Group`.
* Go to `Users`. We create a user that the Django app will use to have S3 access.
  * `Add User`.
  * Give the user a name.
  * Give the user `Programmatic access`.
  * Click `Next: Permissions`.
  * Check the box next to the group you created and click `Next: Tags`.
  * Click on `Next: Review`.
  * Click on `Create user`.
* On the User page, you will need the `Access key ID` and `Secret access key`.
* We need 2 new packages in the app to interact with S3.
  * `pip install django-storages boto3`
* Update the `requirements.txt` file:  `pip freeze > requirements.txt`
* In the main app's `settings.py`:
  * In `INSTALLED_APP` add `'storages',`.
  * At the bottom add:
  ```
  AWS_STORAGE_BUCKET_NAME = getenv("AWS_STORAGE_BUCKET_NAME") 
  AWS_S3_REGION_NAME = getenv("AWS_S3_REGION_NAME")  
  AWS_ACCESS_KEY_ID = getenv("AWS_ACCESS_KEY_ID")
  AWS_SECRET_ACCESS_KEY = getenv(" AWS_SECRET_ACCESS_KEY") 
  AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com" 
  STATICFILES_STORAGE = "stoages.backends.s3boto3.S3Boto3Storage" 
  ```
  * I set them up to use environment variables, which you should as well.
  * `AWS_STORAGE_BUCKET_NAME` is the unique bucket name you setup.
  * The `AWS_S3_REGION_NAME` can be found in the `Properties` tab under `Bucket overview` in the `Region` field.
  * The `AWS_SECRET_ACCESS_KEY` and `AWS_SECRET_ACCESS_KEY` are the User-specific ones from a few steps ago.
  * `STATICFILES_STORAGE` is a Django setting that tells Django how files are stored, we use the S3 Boto Storage to move the files to S3.
* Run:  `python manage.py collectstatic`
  * This will collect all of the static files, like before, but it will also upload them to the S3 bucket.
  * You can verify by going to the bucket and you should see the files in there now.
* We run the server locally:  `python mangage.py runservers --nostatic`
  * This runs the local environment without serving the static files with Django.
  * We will see the styling and images that are in static, which means S3 served them.
  * You can verify by inspecting the page and seeing they are served from the S3 bucket.
* Resources:
  * [https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html)
  * [https://django-storages.readthedocs.io/en/latest/](https://django-storages.readthedocs.io/en/latest/)
  * [https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
  * [https://docs.aws.amazon.com/AmazonS3/latest/user-guide/add-cors-configuration.html](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/add-cors-configuration.html)

# Moving File Uploads to S3

* There is also the `DEFAULT_FILE_STORAGE` setting in the `settings.py` file, which controls the `media` files.
* However, we can't use `"storages.backends.s3boto3.S3Boto3Storage"`, otherwise it will create a security risk because people can overwrite our files with malicious code.
* We create our own storage system that uses S3Boto3Storage, but gives us more control under the hood.
* In the top-level project folder, add the `custom_stores.py` file, with this code:
  ```
  from django.conf import settings
  from storages.backends.s3boto3 import S3Boto3Storage
  class StaticFileStorage(S3Boto3Storage):
      location = settings.STATICFILES_FOLDER
  class MediaFileStorage(S3Boto3Storage):
      location = settings.MEDIAFILES_FOLDER
  ```
* In the main `settings.py` file:
  * Add:  `STATICFILES_FOLDER = "static"`
    * This is the folder name for the static files in the S3 bucket.
  * Add:  `MEDIAFILES_FOLDER = "media"`
    * This is the folder name for the uploaded files in the S3 bucket.
  * Change:   `STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"`   to:   `STATICFILES_STORAGE = "custom_storages.StaticFileStorage"`
  * Add:  `DEFAULT_FILE_STORAGE = "custom_storages.MediaFileStorage"`
* Go to the bucket, select all of the files and click `Delete`. It will prompt you to type `permanently delete` and then you can click `Delete objects`.
* Run:  `python manage.py collectstatic`
* Now in the bucket, the static files will be inside of the `static` folder that wasn't there before.
* We run the local server with `python mangage.py runservers --nostatic` to test if the static files work.
* We edit the post we made before to upload an image and see that it works through S3.
* Now in the bucket, the uploaded files will be inside of the `media` folder that wasn't there before.
* We create a `code.zip` file with the following files/folders.
  * `.ebextensions` folder, `blog` folder, `custom_storage.py` file, `manage.py` file, `my_site` folder, `requirements.txt` file, `templates` folder
* We go back to the `Elastic Beanstalk` console.
  * Go to the application by clicking on the name under the `Applications` tab.
  * Click on `Update and deploy`.
  * Upload the `code.zip` file.
  * Click `Deploy`.
* Go to the site to make sure the static files work.
* Add a new post to see if uploads work.
* That is it, everything is fully deployed.
* Resources:
  * [https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html)
  * [https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)