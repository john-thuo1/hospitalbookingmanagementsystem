"""
Django settings for djangohospitalappointment project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG')
 
# On the allowed hosts, create a url via Ngrok and copy the second part after https://, As shown
# Ngrok site Url https://4af2-41-216-97-217.in.ngrok.io
ALLOWED_HOSTS = ['127.0.0.1', '2971-41-186-78-88.eu.ngrok.io']



# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django_extensions',

    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hospital.apps.HospitalConfig',
    'rest_framework',
    'users.apps.UsersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangohospitalappointment.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'djangohospitalappointment.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        
        
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
TIME_INPUT_FORMATS = ['%I:%M %p',]


USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = 'static/'


MEDIA_ROOT= os.path.join(BASE_DIR, 'media')
MEDIA_URL= '/media/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'


LOGIN_REDIRECT_URL = 'home-page'

# This will redirect someone trying to access e.g profile page without having logged in, to login page
LOGIN_URL = 'login'
# the route the user will automatically be redirected if they access a page without logging in
#------------------------------------------------------

# API Data Interaction
'''
12.	Data is sent from Africa’s Talking U.S.S.D. A.P.I. to our Django project A.P.I. in the form “Content-Type: application/x-www-form-urlencoded”. 
We have to inform our Django A.P.I. to expect data to be sent to it in this format as the default format Django rest framework A.P.I. expects data is JSON format.

13.	Data should also be sent back from our Django A.P.I. to Africa’s Talking USSD A.P.I. in a string format or as a plain text. 
Django rest framework A.P.I. sends data out in JSON format by default, we have to inform or configure our A.P.I. to send data in plain text and not JSON format.

'''
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
    'DEFAULT_RENDERER_CLASSES': [
       
        'api.renders.PlainTextRenderer',
    ],
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
# GRAPH_MODELS = {
#   'all_applications': True,
#   'group_models': True,
# }


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
