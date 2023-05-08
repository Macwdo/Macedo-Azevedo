import os
from datetime import timedelta
from pathlib import Path
import boto3
from dotenv import load_dotenv
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from json import loads

sentry_sdk.init(
    dsn=os.environ.get("DSN"),
    integrations=[
        DjangoIntegration(),
    ],
)

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True if os.environ.get("DEBUG") == "1" else False

ALLOWED_HOSTS = ["*"]

CORS_ALLOWED_ORIGINS = loads(os.environ.get("CORS_ALLOWED_ORIGINS", []))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'django_rest_passwordreset',
    'easyaudit',
    'drf_yasg',
    'storages',

    'processo',
    'cliente',
    'advogado',
    'django_celery_beat',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'easyaudit.middleware.easyaudit.EasyAuditMiddleware',

]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'USER': os.environ.get('DATABASE_USER'),
        'PORT': os.environ.get('DATABASE_PORT')
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

TRACKED = ["8.19"]

# Sentry

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

# Rest Framework

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 15,

}
if not DEBUG:
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = (
        'rest_framework.renderers.JSONRenderer',)

# EMAIL

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = os.environ.get("EMAIL_HOST_USER")

EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = os.environ.get("EMAIL_HOST")

# AWS CONFIG

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_KEY')
AWS_REGION = os.environ.get('AWS_REGION')

# AWS CLOUDWATCH


boto3_logs_client = boto3.client(
    "logs",
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,

)


# AWS S3

if not DEBUG:
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_BUCKET_NAME')
    AWS_S3_FILE_OVERWRITE = False

    AWS_S3_REGION_NAME = AWS_REGION

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "loggers": {
        "processo": {
            "handlers": ["cloud_watch"],
            "level": "INFO"
        },
        "lawsuits_scraping": {
            "handlers": ["cloud_watch"],
            "level": "INFO"
        }

    },
    "handlers": {
        "cloud_watch": {
            "level": "INFO",
            "class": "watchtower.CloudWatchLogHandler",
            'boto3_client': boto3_logs_client,
            "log_group": os.environ.get('AWS_LOG_GROUP'),
            "stream_name": os.environ.get('AWS_LOG_STREAM_NAME'),
            "formatter": "simple",
        },

    },
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {name} {module} {funcName} {message}",
            "datefmt": "[%d/%b/%Y %H:%M:%S]",
            "style": "{",
        },
        "simple": {
            "format": "{asctime} {levelname} {message}",
            "datefmt": "[%d/%b/%Y %H:%M:%S]",
            "style": "{",
        },
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILE_DIRS = [
    os.path.join(BASE_DIR, "staticfiles")
]


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# SIMPLE JWT

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'BLACKLIST_AFTER_ROTATION': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION'
}


# Api Swagger

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    }
}

# Celery

CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_BROKER_URL = os.environ.get(
    "CELERY_BROKER_URL", "pyamqp://guest@localhost//"
)
