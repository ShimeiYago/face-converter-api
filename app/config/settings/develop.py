from .base import *
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r%y1co!o*bnb^i6(-^bchiz!xj$+6fsqk0&v9arnti$3n4m&=2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Email backend
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # output to console for develop

# Master email
# MASTER_EMAIL = "master@master.com"

# For debug if needed
# import datetime
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=1),
#     'REFRESH_TOKEN_LIFETIME': datetime.timedelta(minutes=2),
# }