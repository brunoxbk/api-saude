"""
Django settings for api_saude project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
from decouple import config

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = PROJECT_DIR

ON_RENDER = 'RENDER' in os.environ

SECRET_KEY = os.environ.get('SECRET_KEY')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


DEBUG_MAIL = os.environ.get("DEBUG_MAIL", default=True)

DEBUG = config("DEBUG", default=False, cast=bool)


ALLOWED_HOSTS = ['*', ]

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


INSTALLED_APPS = [
    "home",
    "search",
    'wagtail.api.v2',
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    #
    "rest_framework",
    "rest_framework.authtoken",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    # others
    "corsheaders",
    "chat",
    # "socketio_app"
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    'django_currentuser.middleware.ThreadLocalUserMiddleware',
]

CORS_ALLOW_ALL_ORIGINS=True

ROOT_URLCONF = "api_saude.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
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

WSGI_APPLICATION = "api_saude.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# if not ON_RENDER:
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.%s" % os.environ.get("DB_ENGINE"),
#             "NAME": os.environ.get("DB_NAME"),
#             "USER": os.environ.get("DB_USER"),
#             "PASSWORD": os.environ.get("DB_PASSWORD"),
#             "HOST": os.environ.get("DB_HOST"),
#             "PORT": os.environ.get("DB_PORT"),
#         }
#     }
# else:
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get("DB_URL"),
        conn_max_age=600
    )
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "pt-BR"

TIME_ZONE = "America/Fortaleza"

USE_I18N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

if DEBUG:
    STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


if ON_RENDER:

    # Default storage settings, with the staticfiles storage updated.
    # See https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STORAGES
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        # ManifestStaticFilesStorage is recommended in production, to prevent
        # outdated JavaScript / CSS assets being served from cache
        # (e.g. after a Wagtail upgrade).
        # See https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#manifeststaticfilesstorage
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
        },
    }

REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'jwt-auth',
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

if DEBUG_MAIL:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool, default=False)
EMAIL_HOST = config('EMAIL_HOST', cast=str, default='')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', cast=str, default='')
EMAIL_PORT = config('EMAIL_PORT', cast=int, default=587)
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', cast=str, default='')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', cast=str, default='')

# Wagtail settings

WAGTAIL_SITE_NAME = "api_saude"

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
if ON_RENDER:
    WAGTAILADMIN_BASE_URL = RENDER_EXTERNAL_HOSTNAME
else:
    WAGTAILADMIN_BASE_URL = "http://localhost:8000"

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

