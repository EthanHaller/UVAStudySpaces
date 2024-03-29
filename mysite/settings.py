"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 5.1.dev20230922190154.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from pathlib import Path
import os
import sys
from dotenv import load_dotenv, find_dotenv


"""
 REFERENCES

 Title: Set up Google Sign-In for Faster Django Login Experience feat. Tech with Tim
 Author: TechWithTime
 Date: 12/12/2022
 Code version: N/A
 URL: https://www.youtube.com/watch?v=yO6PP0vEOMc
 Software License: N/A

 Title: DATABASES
 Author: Django Project
 Date: N/A
 Code version: N/A 
 URL: https://docs.djangoproject.com/en/dev/ref/settings/#databases
 Software License: N/A

 Title: Provisioning a Test PostgreSQL database on Heroku for your Django App
 Author: Sola-Aremu 'Pelumi
 Date: 04/15/2020
 Code version: N/A
 URL: https://medium.com/analytics-vidhya/provisioning-a-test-postgresql-database-on-heroku-for-your-django-app-febb2b5d3b29
 Software License: N/A

 Title: AUTH_PASSWORD_VALIDATORS
 Author: Django Project
 Date: N/A
 Code version: N/A
 URL: https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
 Software License: N/A

 Title: Internationalization and localization
 Author: Django Project
 Date: N/A
 Code version: N/A
 URL: https://docs.djangoproject.com/en/dev/topics/i18n/
 Software License: N/A

 Title: How to manage static files (e.g. images, JavaScript, CSS)
 Author: Django Project
 Date: N/A
 Code version: N/A
 URL: https://docs.djangoproject.com/en/dev/howto/static-files/
 Software License: N/A

 Title: DEFAULT_AUTO_FIELD
 Author: Django Project
 Date: N/A
 Code version: N/A
 URL: https://docs.djangoproject.com/en/dev/ref/settings/#default-auto-field
 Software License: N/A
 
 Title: Making Django Messages Work with Bootstrap Toast: A Guide
 Author: Cody Stith
 Date: 05/20/2023
 Code version: N/A
 URL: https://copyprogramming.com/howto/django-messages-bootstrap-toast-how-to-make-it-work
 Software License: N/A
 """

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(find_dotenv())

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'studyspaces-7253e4d961eb.herokuapp.com']

# Application definition

SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'study_spaces',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'bootstrap5',
    'django_bootstrap_icons',
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': os.environ.get("CLIENT_ID"),
            'secret': os.environ.get("CLIENT_SECRET"),
            'key': '',
        },
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

SOCIALACCOUNT_QUERY_EMAIL = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware'
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'study_spaces.context_processors.user_context_processor',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


from urllib.parse import urlparse
DATABASE_URL = os.environ.get("HEROKU_POSTGRESQL_ROSE_URL")
url_parts = urlparse(DATABASE_URL)

DATABASE_USER = url_parts.username
DATABASE_PASSWORD = url_parts.password
DATABASE_HOST = url_parts.hostname
DATABASE_PORT = url_parts.port
DATABASE_NAME = url_parts.path[1:]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT':  DATABASE_PORT
    }
}

if "test" in sys.argv:
    DATABASES["default"] = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
    ]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

AUTHENTICATION_BACKENDS = [
  'django.contrib.auth.backends.ModelBackend',
  'allauth.account.auth_backends.AuthenticationBackend',
]

from django.contrib import messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

LOGIN_REDIRECT_URL = "/study/"
LOGOUT_REDIRECT_URL = "/study/logout/"
SOCIALACCOUNT_LOGIN_ON_GET=True
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")