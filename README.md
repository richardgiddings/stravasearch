# README

Get activities from Strava for an athlete. Uses [social-auth-app-django](https://github.com/python-social-auth/social-app-django) to authenticate a user then [stravalib](https://github.com/hozn/stravalib) to retrieve the activities for that user. Activities are displayed on the page with pagination. 

The first time you visit the site there are no activities shown. If you just specifiy a From date then activities after that date are retrieved. If you just specify a To date then activities up until that date are retrieved. If you specify both you get activities in that range of dates. If you specify neither then nothing is retrieved.

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