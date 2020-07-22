import os
# message import
from django.contrib.messages import constants as messages

# herokuapp
import django_heroku
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'so2(!vq2#a*w&gyb2lgkprt4w3tln19nrr%dq_3rpoodtp2cup'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['hbtre.herokuapp.com', '127.0.0.1:8000']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'pages.apps.PagesConfig',
    'listings.apps.ListingsConfig',
    'realtors.apps.RealtorsConfig',
    'accounts.apps.AccountsConfig',
    'inquiry.apps.InquiryConfig',

    'django.contrib.humanize',  # makes the prices easier to read i.e, commas

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

ROOT_URLCONF = 'btRE.urls'

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

WSGI_APPLICATION = 'btRE.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#       'NAME': 'btre',
#        'USER': 'postgres',
#        'PASSWORD': '0000',
#        'HOST': 'localhost',
#        # 'PORT': '5432',
#    }
# }

# new DATABASES
DATABASES = {
    'default': dj_database_url.config()
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# creates 'static' folder in the root dir (Housing) after running collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

# location of 'static' in btRE folder
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'btRE/static')
]

# media settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # creates a 'media' folder in the root dir (Housing) directory
MEDIA_URL = '/media/'

# messages
MESSAGE_TAGS = {
    messages.ERROR: 'alert-danger',  # value is equal to the bootstrap class of 'alert-danger'
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
}

# email config
# EMAIL_HOST = ''
# EMAIL_PORT =
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = True

# new
django_heroku.settings(locals())
