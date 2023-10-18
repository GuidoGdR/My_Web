from core.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.guidodorego.com', 'guidodorego.com']

CSRF_TRUSTED_ORIGINS = ['https://*.guidodorego.com','https://guidodorego.com']
