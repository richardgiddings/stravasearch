#
#   Production settings
#

from .base import *

import os
import dj_database_url

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

# Allow all host headers for now until we have a domain name
ALLOWED_HOSTS = ['strava-search.herokuapp.com']

DEBUG = False

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Where collectstatic puts files
STATIC_ROOT = os.path.join(os.path.dirname(PROJECT_DIR), 'staticfiles')

# URL to use when referring to static files located in STATIC_ROOT.
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

# email settings
EMAIL_HOST = env['EMAIL_HOST']
EMAIL_PORT = env['EMAIL_PORT']
EMAIL_HOST_USER = env['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = env['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = env['DEFAULT_FROM_EMAIL'] # e.g 'Admin <noreply@example.com>'
SERVER_EMAIL = EMAIL_HOST_USER

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ADMINS = ((env['ADMIN_NAME'], env['ADMIN_EMAIL']),)

CSRF_COOKIE_SECURE = True