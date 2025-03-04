"""
Django settings for auth_service project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
import os
from dotenv import load_dotenv
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rhzjsf3rtqp+vwntza3dq_ty!ujq7os2nvk#m-b$d*&0%#)8kw'

JWT_SIGNING_KEY="""
-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC9cvHLt9VLsT3T
VB2Kt0wqs//+m52u/m2i95+SE0IrMvQjTL5xxcwvw84iYfPVdM+t4HjK6MobBgPx
X4W7m7YLLpwwsfSIci6OhAZ8UQHKYhZSS033MSL+6Jj8Jb2ZSVjzDE8/G8+CM7Vn
VVPK4GmSJ8gsSroghO0/CYe60N1vwxmQbGvfZG6EeSJMaiHpEZC7u2Du+s0YaOCJ
rY7LLVifowpg2K9UC1a3d12gzVc2xbpc1jkBfN0tvmWVEWn4+Gr/ki1Fuu/dygw8
bC3P/0VOlN3/T3cErxzozQyV61vFkuyU3hDpKSG4OcRgxTWlb64l2wCif8bGVKVY
+iM1vvMdAgMBAAECggEACU1GAwR9NBC5TObckSLhL1g+3FpOr+NtMFXBNNO+Ps8V
0/qLf/GVeM4/5knx8Mv3UH3CNeWf2sYnq70kHKs6ESrSNMU1ZlJY59rNU2L02Azg
igeJhfbDKvSdDQWwsqs6c1XqOYUyN0iLrSMFkLixEPc5abdSPpDYR0KUB/+uXQjd
LRz+7GAePA3a/f9rKNPt2rcd9mOQLANLL5oLbcSrnxRqrai4tN+H6VHc5yc/doKJ
FGBbhYZWq3/bTevINv6MiP1ivGeuhJGTp5utPnpVm30ZTU73khShpvrZIFgW3RvY
jpxg46JtSyCQ3i5qJjowFOP2hmDv44+PzcvZnkV7cQKBgQDfXOjuMWHziRkbZYt5
V4lQoPjty4m793JVxoMr+uuaCsKU064WwqOF1V6+PpL9M9O7XzCdQmqepuK7JrWo
VKpwQ1PDW5dSKfwMgezKHVeL1WPME3FXGvvm4MBEs0zo9iOxCxAiDZ8cn3ZbIJO6
bZmCIcDhOIi5TllqOBCl3Na1RQKBgQDZIXQvxwpLckdSKSyO9UoJL4oVP3TydCEF
0XsN0naXlDKRT4f+LkkcaFbl0QnQFF5KwyNUSZBhCm3rclDtB/6ejXiGcGXCn4zM
OjZyoQONd1UL17frqrpn2f/2ty1XmXOwFDYqXWquKd2tsIgDPEPUVqAQI22H63Y1
tBfFmgDH+QKBgFmKRVY3Na0LKKVy75aVINbRsPiiv3Q6nfsEuVDIJep6pcZDlWZK
YIMmJfTd4M7gF+DlJ/fiyBsRi5K60dfJGQon80w9S0wEyKW679GWMaI8yOTmZmkk
yBalwm3H8uzwvx4Z8T21eDNhOXEOfioeBYvFPC0NHMIsRmvuTb4v6WKBAoGAZvAj
Qxtb2BTflyYKB+RmKyCsmBIzgVZo6Xc8nXrv2kDaEGXiFTEgXCVjPSTzQADICy2k
LCuMFVV6cysJDrbBka2EPEhBFhnKCHB4q7OGGaU/XpPwj/uqz91cKj0BdAw9+nY6
j68mCleyzstoUBBcH+jJjZ0eKlgI/MDanEW8pRECgYBYCNtgvqh86Jk6YGDumdii
yDI0xTun0Bezsf07jnnCSZaYf2nQ3qEDSXUzoXXqvbioDemr28WOlSPrsTwJXOBD
Er3PbrOnDYWu5j08IECxT0USUZ5mnL39xOvvPF2RJ54HNr1HqYlopBgN3LA5LwK/
1cYCKohZaqGs35dmNk8Uew==
-----END PRIVATE KEY-----
"""

JWT_VERIFYING_KEY="""
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvXLxy7fVS7E901QdirdM
KrP//pudrv5tovefkhNCKzL0I0y+ccXML8POImHz1XTPreB4yujKGwYD8V+Fu5u2
Cy6cMLH0iHIujoQGfFEBymIWUktN9zEi/uiY/CW9mUlY8wxPPxvPgjO1Z1VTyuBp
kifILEq6IITtPwmHutDdb8MZkGxr32RuhHkiTGoh6RGQu7tg7vrNGGjgia2Oyy1Y
n6MKYNivVAtWt3ddoM1XNsW6XNY5AXzdLb5llRFp+Phq/5ItRbrv3coMPGwtz/9F
TpTd/093BK8c6M0MletbxZLslN4Q6SkhuDnEYMU1pW+uJdsAon/GxlSlWPojNb7z
HQIDAQAB
-----END PUBLIC KEY-----
"""


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
    'rest_framework',
    'rest_framework_simplejwt',
    'users',
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

ROOT_URLCONF = 'auth_service.urls'

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

WSGI_APPLICATION = 'auth_service.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgresql_db",
        "USER": "admin",
        "PASSWORD": "admin",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME': timedelta(days=30),
    'SLIDING_TOKEN_REFRESH_LIFETIME_LATE_USER': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME_LATE_USER': timedelta(days=30),
    'SIGNING_KEY' : JWT_SIGNING_KEY,
    'VERIFYING_KEY' : JWT_VERIFYING_KEY,
    'ALGORITHM' : 'RS256',  # Default would be HS256
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "users.User"

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWS_CREDENTIALS = True