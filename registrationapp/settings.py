"""
Django settings for registrationapp project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY',"django-insecure-!w@=nmm-w17=akin9o$a=ceuj1ff0vtlxcw-kjdlg$n)n9&du9")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'WEBSITE_HOSTNAME' not in os.environ

if DEBUG:
    ALLOWED_HOSTS = []
    
else:
    ALLOWED_HOSTS = ["https://successdjango.azurewebsites.net","successdjango.azurewebsites.net"]
    CRSF_TRUSTED_ORIGINS = ["https://successdjango.azurewebsites.net"]
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO',"https")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "studentreg.apps.StudentregConfig",
    'crispy_forms',
    'storages',
    'rest_framework',

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "registrationapp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "registrationapp.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['AZURE_DB_NAME'],
            'HOST': os.environ['AZURE_DB_HOST'],
            'PORT': os.environ['AZURE_DB_PORT'],
            'USER': os.environ['AZURE_DB_USER'],
            'PASSWORD': os.environ['AZURE_DB_PASSWORD'],
            
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
if DEBUG:
    STATIC_URL = "static/"
    MEDIA_ROOT = BASE_DIR / "media"
    MEDIA_URL = "/media/"
else:
    AZURE_SA_NAME = os.environ['AZURE_SA_NAME']
    AZURE_SA_KEY = os.environ['AZURE_SA_KEY']
    DEFAULT_FILE_STORAGE = 'registrationapp.storages.AzureMediaStorage'
    STATICFILES_STORAGE = 'registrationapp.storages.AzureStaticStorage'
    STATIC_URL = f'https://{AZURE_SA_NAME}.blob.core.windows.net/static/'
    MEDIA_URL = f'https://{AZURE_SA_NAME}.blob.core.windows.net/media/'


CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Redirect to the student dashboard after login
LOGIN_REDIRECT_URL = "profile"

# Required to redirect user when they hit login_required page
LOGIN_URL = "login"



# EMAIL_BACKEND setting to use the SMTP backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# email address from which the password reset emails will be sent
DEFAULT_FROM_EMAIL = 'nanaothman001@gmail.com'

# Email configuration for the SMTP backend
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587  # gmail port for SMTP server
EMAIL_USE_TLS = True 

# authentication credentials for the SMTP server
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL
EMAIL_HOST_PASSWORD = 'oicqcneeghndyubq'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}