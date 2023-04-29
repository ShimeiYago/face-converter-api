from pathlib import Path
import os
import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
env_file = os.path.join(BASE_DIR, '.django-env')
env.read_env(env_file)

# Add common settings

# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    # 'dj_rest_auth',
    'django.contrib.sites',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.twitter',
    # 'allauth.socialaccount.providers.google',
    # 'dj_rest_auth.registration',
    'corsheaders',
    # 'django_cleanup.apps.CleanupConfig',
    # 'users',
    # 'auths',
    # 'articles',
    'convert',
    # 'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'config.admin-middleware.AdminProtect',  # to restrict access to admin
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'auths/templates'),
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'

# logging
LOG_BASE_DIR = os.path.join(BASE_DIR, "log")  #log output dir
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"simple": {"format": "%(asctime)s [%(levelname)s] %(message)s"}},
    "handlers": {
        "error": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOG_BASE_DIR, "error.log"),
            "formatter": "simple",
        },
    },
    "root": {
        "handlers": ["error"],
        "level": "INFO",
    },
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

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, STATIC_URL)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_NAME = "Face Converter"

CLIENT_ORIGIN_URL = env('CLIENT_ORIGIN_URL')  # Ex: http://127.0.0.1:3000

# Security
ALLOWED_HOSTS = [env('ALLOWED_HOST')] # Ex: 127.0.0.1
CORS_ORIGIN_WHITELIST = [CLIENT_ORIGIN_URL]

SITE_ID = 1

### Authentications ###

# AUTHENTICATION_BACKENDS = [
#     # allauth specific authentication methods, such as login by e-mail
#     'allauth.account.auth_backends.AuthenticationBackend',
#     # Needed to login by username in Django admin, regardless of allauth
#     'django.contrib.auth.backends.ModelBackend',
# ]

# AUTH_USER_MODEL = 'users.CustomUser'

# REST_AUTH_REGISTER_SERIALIZERS = {
#     'REGISTER_SERIALIZER': 'users.serializers.CustomRegisterSerializer',
# }

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

# set based on docker-compose.yml
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'trivia-map-db',
#         'USER': 'django',
#         'PASSWORD': 'django',
#         'HOST': 'db',
#         'PORT': '3306'
#     }
# }

# REST_USE_JWT = True
# JWT_AUTH_COOKIE = 'trivia-map-auth' # The cookie key name can be the one you want
# JWT_AUTH_REFRESH_COOKIE = 'trivia-map-refresh-auth'
CORS_ALLOW_CREDENTIALS = True

# REST_AUTH_SERIALIZERS = {
#     'USER_DETAILS_SERIALIZER': 'users.serializers.CustomUserDetailsSerializer',
# }

# ACCOUNT_ADAPTER = 'auths.adapter.CustomAccountAdapter'

# LOGOUT_ON_PASSWORD_CHANGE = False

# allauth configuration
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_CONFIRM_EMAIL_ON_GET = True


# swagger
SWAGGER_SETTINGS = {
    'DEFAULT_INFO': 'config.urls.api_info',
}

API_VERSION = '1.0'

# upload dir
# UPLOAD_DIR = 'uploads'

# login api returns expiration
# JWT_AUTH_RETURN_EXPIRATION = True

# SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
# SOCIALACCOUNT_EMAIL_REQUIRED = False
# SOCIALACCOUNT_QUERY_EMAIL = True

# # twitter api
# TWITTER_API_KEY = env('TWITTER_API_KEY')
# TWITTER_API_KEY_SECRET = env('TWITTER_API_KEY_SECRET')

# # admin
# ADMIN_PATH = env('ADMIN_PATH')
# ALLOWED_IPS_TO_ACCESS_ADMIN = [env('ALLOWED_IP_TO_ACCESS_ADMIN')]