"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from datetime import timedelta
from pathlib import Path
from typing import List

import environ
from rest_framework.reverse import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(env_file=os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS: List[str] = []
ALLOWED_HOSTS += [env("ALLOWED_HOSTS")]

# Application definition

DJANGO_SYSTEM_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

CUSTOM_USER_APPS = [
    "rest_framework",
    "debug_toolbar",
    "django_extensions",
    "drf_spectacular",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "allauth",
    "allauth.account",
    # "allauth.socialaccount",
    "app.activity",
    "app.album",
    "app.board",
    "app.category",
    "app.club",
    "app.comment",
    "app.user",
]

INSTALLED_APPS = DJANGO_SYSTEM_APPS + CUSTOM_USER_APPS

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

INTERNAL_IPS = ["127.0.0.1"]

ROOT_URLCONF = "mysite.urls"

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

# AUTHENTICATION_METHODS = ["allauth.account.auth_backends.AuthenticationBackend"]

WSGI_APPLICATION = "mysite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": env("DB_ENGINE"),
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "user.User"

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
        # "rest_framework.permissions.IsAdminUser",
        # "rest_framework.permissions.AllowAny",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": False,  # True - 새로운 리프레시 토큰이 발급될 때마다 이전의 리프레시 토큰이 만료됨
    "BLACKLIST_AFTER_ROTATION": False,  # True - 리프레시 토큰이 새로 발급되면 이전의 리프레시 토큰을 블랙리스트에 추가하는 옵션
    "UPDATE_LAST_LOGIN": True,  # True - 마지막 로그인 시간을 업데이트
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,  # SECRET_KEY를 이용해 JWT 서명에 사용되는 비밀키 지정
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",  # user 모델에서 사용자 식별하는 필드
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",  # JWT 토큰에 저장되는 사용자 정보의 클래스 지정
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
    # "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    # "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    # "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    # "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    # "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    # "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

# AUTHENTICATION_BACKENDS = [
#    # Needed to login by username in Django admin, regardless of `allauth`
#    "django.contrib.auth.backends.ModelBackend",
#    # `allauth` specific authentication methods, such as login by email
#    "allauth.account.auth_backends.AuthenticationBackend",
# ]

# SOCIALACCOUNT_PROVIDERS = {
#     "google": {
#         "APP": {
#             "client_id": env("SOCIAL_AUTH_GOOGLE_CLIENT_ID"),
#             "secret": env("SOCIAL_AUTH_GOOGLE_SECRET"),
#             "key": ""
#         }
#     }
# }


# SOCIALACCOUNT_LOGIN_ON_GET = True
# LOGIN_REDIRECT_URL = "/"
# ACCOUNT_LOGOUT_REDIRECT_URL = reverse_lazy("user:login")
# LOGOUT_REDIRECT_URL = "/"
# ACCOUNT_LOGOUT_REDIRECT_URL = "/"
# ACCOUNT_LOGOUT_ON_GET = True

# 필수
SITE_ID = 1
REST_USE_JWT = True  # debug
ACCOUNT_USER_MODEL_USERNAME_FIELD = None  # username 필드 사용 x
ACCOUNT_EMAIL_REQUIRED = True  # email 필드 사용 o
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_VERIFICATION = "none"
# 필수 아님
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_ADAPTER = "app.user.adapters.CustomAccountAdapter"
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"  # ?

REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_HTTPONLY": False,  # 쿠키를 http only로 안함(기본 True)
    "JWT_AUTH_COOKIE": "access",
    "JWT_AUTH_REFRESH_COOKIE": "refresh",  # refresh token 담을 쿠키 이름
    "JWT_AUTH_COOKIE_USE_CSRF": True,  # JWT 쿠키 csrf 검사
    "SESSION_LOGIN": False,  # sessionid가 쿠키로 남지 않음
    "REGISTER_SERIALIZER": "app.user.serializers.SignupSerializer",
}

# REST_AUTH_REGISTER_SERIALIZER = {
#     "REGISTER_SERIALIZER": "user.serializers.SignupSerializer",
# }

# STORAGES = {
#     "default": {
#         "BACKEND": "storages.backends.s3.S3Storage",
#         "OPTION": {
#             "session_profile": env("STORAGE_SESSION_PROFILE"),
#             "access_key": env("AWS_ACCESS_KEY_ID"),
#             "secret_key": env("AWS_SECRET_ACCESS_KEY"),
#             "bucket_name": env("AWS_STORAGE_BUCKET_NAME"),
#         }
#     },
#     "staticfiles": {
#         "BACKEND": "storages.backends.s3.S3Storage",
#         "OPTION": {
#
#         }
#     }
# }

STATIC_ROOT = BASE_DIR / "static"
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

# DEFAULT_FILE_STORAGE = env("DEFAULT_FILE_STORAGE")
# STATICFILES_STORAGE = env("STATICFILES_STORAGE")
# AWS_S3_SESSION_PROFILE = env("STORAGE_SESSION_PROFILE")
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_REGION_NAME = env("AWS_REGION_NAME")
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
# AWS_DEFAULT_ACL = env("AWS_DEFAULT_ACL")
# AWS_QUERYSTRING_AUTH = False

SPECTACULAR_SETTINGS = {
    "TITLE": "Landing",
    "DESCRIPTION": "Project Description",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "console": {
#             "level": "DEBUG",
#             "class": "logging.StreamHandler",
#         },
#     },
#     "loggers": {
#         "django.db.backends": {
#             "handlers": ["console"],
#             "level": "DEBUG",
#         },
#     },
# }
