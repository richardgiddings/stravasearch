# README

Get activities from Strava for an athlete. Uses [social-auth-app-django](https://github.com/python-social-auth/social-app-django) to authenticate a user then [stravalib](https://github.com/hozn/stravalib) to retrieve the activities for that user. Activities are displayed on the page with pagination.

![Alt text](site.png?raw=true "site")

The following config variables are required when deploying to production:
* ADMIN_EMAIL
* ADMIN_NAME
* DEFAULT_FROM_EMAIL
* DJANGO_SETTINGS_MODULE set as stravasearch.settings.production
* EMAIL_HOST
* EMAIL_HOST_PASSWORD
* EMAIL_HOST_USER
* EMAIL_PORT
* SECRET_KEY

Then the following two variables that are given to you when you create an application on strava.com

* STRAVA_SECRET
* STRAVA_KEY