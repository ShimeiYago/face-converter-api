from .base import *
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Email backend (add SMTP server infomation)
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.googlemail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = env('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

### AWS S3 ###
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
# AWS_S3_CUSTOM_DOMAIN = env('AWS_S3_CUSTOM_DOMAIN')  # example.com

# Master email
# MASTER_EMAIL = env('MASTER_EMAIL')

### TODO: May be needed?
# JWT_AUTH_SAMESITE = None  # default='Lax'
# JWT_AUTH_SECURE = True
# CSRF_COOKIE_SAMESITE = None  # default='Lax'
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SAMESITE = None  # default='Lax'
# SESSION_COOKIE_SECURE = True
