import os
from django.contrib.messages import constants as message_constants
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__name__))
MEDIA_ROOT = f'{PROJECT_ROOT}/media'
DOCUMENT_MEDIA_ROOT = 'DOCUMENTS'

DISTRIBUTOR_MEDIA_ROOT = f'{DOCUMENT_MEDIA_ROOT}/DISTRIBUTOR'
RETAILER_MEDIA_ROOT = f'{DOCUMENT_MEDIA_ROOT}/RETAILER'
EMPLOYEE_MEDIA_ROOT = f'{DOCUMENT_MEDIA_ROOT}/EMPLOYEE'

IMAGE_MEDIA_ROOT = 'IMAGES/IMAGE'
LOGO_MEDIA_ROOT = 'IMAGES/LOGO'
PRODUCT_MEDIA_ROOT = 'IMAGES/PRODUCT'

TENANT_ID_STRING_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
DISTRIBUTOR_CODE_STRING_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHA_NUMERIC_STRING_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY123456789"

# AUTH_USER_MODEL = "profile.DocoUser"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zn#)j@7_vgs9ns26gvgx+4@z8-0z5koi$&*v-6lm(_^21jqf&#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS = ['127.0.0.1', 'fed7-103-230-104-31.ap.ngrok.io']
ALLOWED_HOSTS = ['*']
# CSRF_TRUSTED_ORIGINS = ['https://admin.mydoco.in', 'https://127.0.0.1', 'https://0.0.0.0:8000']
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'rest_framework_simplejwt',

    'apps.common',
    'apps.profile',
    'apps.sells',
    'apps.stock',
    # 'apps.ui',
    'apps.api',
    'apps.configuration',

]

MIDDLEWARE = [
    # '**corsheaders.middleware.CorsMiddleware**',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = ['doco.middleware.UsernameEmailSettingsBackend']
ROOT_URLCONF = 'doco.urls'
AUTH_USER_MODEL = 'profile.DocoUser'

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

WSGI_APPLICATION = 'doco.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

STAGE_DB = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'HOST': os.environ.get('DATABASE_HOST', "demo-django.cywh4dxyqcdh.ap-south-1.rds.amazonaws.com"),
    'NAME': os.environ.get('DATABASE_NAME', "doco_stage"),
    'USER': os.environ.get('DATABASE_USER', "doco"),
    'PASSWORD': os.environ.get('DATABASE_PASSWORD', "kmpekb1KcW3cTzD"),
    'PORT': os.environ.get('DATABASE_PORT', '5432'),
    'ATOMIC_REQUESTS': True,
    'CONN_MAX_AGE': 0,
}
DEFAULT_DB = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}
DATABASES = {
    'default': STAGE_DB
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAdminUser'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 1
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

REST_USE_JWT = True

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'staticfiles'),
# ]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
]

MESSAGE_TAGS = {
    message_constants.ERROR: 'danger',
}

# Employee Management system as distributor
# As super admin manage distributors
# Distributor can create non KYC retailer, Phone number is mandatory, Phone number is the username(Retailer),
# any random password
# Next time retailer wants to register they need to put phone number, get an OTP, and reset password
# - Exclude default Registration system

####
# API
# Login - Response (Profile type, Access Token, etc.)
# Registration (Retailer)
# Get Profile Details (Full profile details in response details, )

# API,
# LOGIN, TOKEN
# ORDER (READ based on tenant), create
# Retailer profile (View, create) - BDE, Distributor

# ----- #
# Inventory
#
#
