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
* **v0.2 (Unexpected HTTP methods fixed)** - Same unit tests as `v0.1`, but passing
* **v0.3 (Authentication check tests failing)** - Unit tests that check to make sure that authentication is properly being enforced on post-auth endpoints (failing)
* **v0.4 (Authentication check tests passing)** - Same unit tests as `v0.3`, but passing
* **v0.5 (Header inclusion check tests failing)** - Unit tests that check to make sure that security headers are present in all responses from the application views (failing)
* **v0.6 (Header inclusion check tests passing)** - Same unit tests as `v0.5`, but passing
* **v0.7 (Header exclusion check tests failing)** - Unit tests that check to make sure that specific HTTP response headers are not found in any responses from the application views (failing)
* **v0.8 (Header exclusion check tests passing)** - Same unit tests as `v0.7`, but passing
* **v0.9 (Options accuracy check tests failing)** - Unit tests that check to make sure that the `Allow` header returned by HTTP responses matches the available HTTP verbs on all views in the application (failing)
* **v0.10 (Options accuracy check tests passing)** - Same unit tests as `v0.9`, but passing
* **v0.11 (CSRF enforcement check tests failing)** - Unit tests that ensure that CSRF security controls are present and being enforced on all non-idempotent HTTP verb handlers (failing)
* **v0.12 (CSRF enforcement check tests passing)** - Same unit tests as `v0.11`, but passing
* **v0.13 (Reflected XSS test failing)** - Unit test for checking for the presence of a reflective cross-site scripting vulnerability (failing)
* **v0.14 (Reflected XSS test passing)** - Same unit test as `v0.13`, but passing
* **v0.15 (Bad new view added, no requestor)** - This tag adds a view to the codebase that does not follow the expected conventions around the `requestor` paradigm demonstrated in the codebase
* **v0.16 (Requestor added to bad new view, tests failing)** - This tag adds a requestor to the view added in `v0.15`, which in turn demonstrates how the dynamic unit test generation catches bad code that has only recently been added to a protected codebase
* **v0.17 (Persistent XSS test failing)** - Unit test for checking for the presence of a persistent cross-site scripting vulnerability (failing)
* **v0.18 (Persistent XSS test passing)** - Same unit test as `v0.17`, but passing
* **v0.19 (SQL injection test failing)** - Unit test for checking for the presence of a SQL injection vulnerability (failing)
* **v0.20 (SQL injection test passing)** - Same unit test as `v0.19`, but passing
* **v0.21 (Open redirect test failing)** - Unit test for checking for the presence of an open redirect vulnerability (failing)
* **v0.22 (Open redirect test passing)** - Same unit test as `v0.21`, but passing