"""
Django settings for BlackBorad project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import sys
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/
import json

with open(os.path.join(BASE_DIR, 'config.json'), 'r') as f:
    ENV = json.load(f)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ENV.get('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG_LEVEL = 'default'
ALLOWED_HOSTS = ['bbh.yangyq.net', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    # 'django.contrib.staticfiles',
    'blackboard',
    'wechat',
    'django_apscheduler'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BlackBorad.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / 'templates']
#         ,
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

WSGI_APPLICATION = 'BlackBorad.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': ENV.get('MYSQL_NAME', ''),
        'HOST': ENV.get('MYSQL_HOST', 'localhost'),
        'PORT': ENV.get('MYSQL_PORT', 3306),
        'USER': ENV.get('MYSQL_USER', ''),
        'PASSWORD': ENV.get('MYSQL_PASS', ''),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = False

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'UNAUTHENTICATED_USER': None,
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',  # application/json
        'rest_framework.parsers.FormParser',  # application/x-www-form-urlencoded
        'rest_framework.parsers.MultiPartParser',  # multipart/form-data
    )
}

FILE_UPLOAD_HANDLERS = [
    "django.core.files.uploadhandler.TemporaryFileUploadHandler"
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# MINIAPP settings
APP_ID = ENV.get('APP_ID', '')
APP_SECRET = ENV.get('APP_SECRET', '')
TEMPLATE_ID = ENV.get('TEMPLATE_ID', '')

ADMINS = [('bai', '3401797899@qq.com'), ]
SERVER_EMAIL = ENV.get('SERVER_EMAIL', '')
EMAIL_HOST = ENV.get('EMAIL_HOST', '')
EMAIL_HOST_PASSWORD = ENV.get('EMAIL_PASS', '')
EMAIL_HOST_USER = SERVER_EMAIL
EMAIL_PORT = ENV.get('EMAIL_PORT', 465)
EMAIL_USE_SSL = True

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse',
#         }
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler'
#         },
#         'null': {
#             'class': 'logging.NullHandler',
#         },
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', ],
#             'level': 'INFO',
#         },
#         'django.security.DisallowedHost': {
#             'handlers': ['null'],
#             'propagate': False,
#         },
#     }
# }
