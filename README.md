# security-unit-testing
This is a repository containing example code for how you can use unit tests to protect against security regression. This code is meant to accompany a talk given at QCon NYC in June of 2017. Once the talk video and slides have been posted online, they will be linked to in this readme.

## Getting Started

This project is a standard Django project. In order to get started (assuming you have Django installed already), do the following from the `sectesting` directory in the project:

```
python manage.py makemigrations streetart
python manage.py migrate
python manage.py createsuperuser
```

You must then copy over the example `settings.py` file and rename it:

```
cp sectesting/sectesting/settings.py.example sectesting/sectesting/settings.py
```

With the `settings.py` file copied over you'll need to populate the `AWS_KEY_ID` and `AWS_SECRET_KEY` fields with AWS key data (if you want the S3 file upload functionality to work).

Once you've done the above you can go ahead and start the web server with the following command:

```
python manage.py runserver
```

The server will now be running at http://127.0.0.1:8000/!

## Commit Tags

This repo contains a number of commit tags that correspond to different examples of unit tests in both failing and passing states. The tags are as follows:

* **v0.1 (Unexpected HTTP methods)** - Unit tests that check to make sure that requestor classes contain functionality for testing all verbs associated with an endpoint (failing)
* **v0.2 (Unexpected HTTP methods fixed)** - Same unit tests as v0.1, but passing
