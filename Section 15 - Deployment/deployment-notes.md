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

* 