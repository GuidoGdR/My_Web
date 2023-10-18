from core.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


#https://docs.djangoproject.com/en/4.2/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT=True

#COOKIE_SECURE
#https://docs.djangoproject.com/es/4.2/ref/settings/#std-setting-CSRF_COOKIE_SECURE
CSRF_COOKIE_SECURE = True

#https://docs.djangoproject.com/es/4.2/ref/settings/#std-setting-SESSION_COOKIE_SECURE
SESSION_COOKIE_SECURE = True
