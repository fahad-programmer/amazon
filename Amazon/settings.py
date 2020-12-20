"""
Django settings for Amazon project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Error Tracking (Sentry SDK)
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jzgr*8ak&pe4$e4b5ytm0y)29%v=!qw5msy_%i#7kb@ngttze$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "Blog",
    "Home",
    "Shop",
    'cart',

    # Geoip
    'geoip2',

    # For The Social Login
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # Sites Used For Social Login (Facebook And Google)
    'allauth.socialaccount.providers.facebook',  # Facebook
    'allauth.socialaccount.providers.google',

    # User-Visit (Tracking The Client To Server Request)
    'user_visit',

    # Sitemap
    'django.contrib.sitemaps',

    # Activity Stream
    'actstream',

    # Notification System
    'notifications',

    # Django Cleaner (Cleans Unused Files)
    'django_cleanup.apps.CleanupConfig',

    # User-Feedback
    'tellme',

    'django_filters',


    # Mobile Authentication
    "phone_verify",

    'rest_framework',


]

# Site Id
SITE_ID = 1

# Provider specific settings

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '805663397466-g2jblik0dnhfm0bit60dq7t0e7fc7265.apps.googleusercontent.com',
            'secret': 'qhv-3E4_20IthPYbeY054joq',
            'key': ''
        },
        'SCOPE': [
            'profile',
            'email',
        ],
    },  'facebook': {

        'APP': {
            'client_id': '1096504117449006',
            'secret': '4458fb4d143ee6294058ef5ac29d5b70',
            'key': ''
        },

        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'name',
            'name_format',
            'picture',
            'short_name'
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v7.0',
    }
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # User Tracking Middleware
    'user_visit.middleware.UserVisitMiddleware',

    # Caches
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'Amazon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Telling Django About Where Our Templates Files Are
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processor.cart_total_amount',
            ],
        },
    },
]

CART_SESSION_ID = 'cart'

WSGI_APPLICATION = 'Amazon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'main',
        'USER': 'postgres',
        'PASSWORD': 'fahad',
        'HOST': 'localhost',
        'PORT':'5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Managing Media Files

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Authentication Backends Are Given Below
AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]


# Connection To Sentry Server
sentry_sdk.init(
    dsn="https://de78fa71c1a64aea95cda70b2cfc97a9@o472385.ingest.sentry.io/5505935",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,

    # to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

# ActStream Settings
ACTSTREAM_SETTINGS = {
    'FETCH_RELATIONS': True,
    'USE_PREFETCH': True,
    'USE_JSONFIELD': True,
    'GFK_FETCH_DEPTH': 1,
}

# Adding Extra Data To Notification
DJANGO_NOTIFICATIONS_CONFIG = {'USE_JSONFIELD': True}


# In settings.py
# Add settings for phone_verify to work
PHONE_VERIFICATION = {
    "BACKEND": "phone_verify.backends.twilio.TwilioBackend",
    "OPTIONS": {
        "SID": "ACdb84efb2452409796286622b88ad1abd",
        "SECRET": "2453000b44ea241ba4ed3c8efc9a586e",
        "FROM": "+15052786084",
        "SANDBOX_TOKEN": "123456",
    },
    "TOKEN_LENGTH": 6,
    "MESSAGE": "Welcome to Amazon! Please use security code {security_code} to proceed.",
    "APP_NAME": "Phone Verify",
    "SECURITY_CODE_EXPIRATION_TIME": 3600,  # In seconds only
    # If False, then a security code can be used multiple times for verification
    "VERIFY_SECURITY_CODE_ONLY_ONCE": False,
}

# Cache To Store Data

# CACHE_TTL = 60 * 115

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': 'django_cache',
#         'OPTIONS': {
#             'MAX_ENTRIES': 10000
#         }
#     }
# }
