import os
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['sound-airport.azurewebsites.net']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_HOST'],
        'PORT': 5432,
    }
}

# Storage

DEFAULT_FILE_STORAGE = 'backend.custom_azure.AzureMediaStorage'
STATICFILES_STORAGE = 'backend.custom_azure.AzureStaticStorage'

STATIC_LOCATION = "static"
MEDIA_LOCATION = "media"

STORAGE_ACCOUNT = os.environ['STR_ACC']
STORAGE_CUSTOM_DOMAIN = f'{STORAGE_ACCOUNT}.blob.core.windows.net'

STATIC_URL = f'https://{STORAGE_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
MEDIA_URL = f'https://{STORAGE_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'

# Auth0 settings

SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

SOCIAL_AUTH_TRAILING_SLASH = False  # Remove trailing slash from routes
SOCIAL_AUTH_AUTH0_DOMAIN = os.environ['AUTH_DOMAIN']
SOCIAL_AUTH_AUTH0_KEY = os.environ['AUTH_KEY']
SOCIAL_AUTH_AUTH0_SECRET = os.environ['AUTH_SECRET']
SOCIAL_AUTH_AUTH0_SCOPE = [
    'openid',
    'profile',
    'email'
]

AUTHENTICATION_BACKENDS = {
    'social_core.backends.auth0.Auth0OAuth2',
    'django.contrib.auth.backends.ModelBackend'
}

LOGIN_URL = '/login/auth0'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
