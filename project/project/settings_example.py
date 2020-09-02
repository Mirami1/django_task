# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ''

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': u'',
        'USER': u'',
        'PASSWORD': u'',
        'HOST': '',
        'PORT': ''
    },
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'Your gmail email'
EMAIL_HOST_PASSWORD = 'Your gmail password'
DEFAULT_FROM_EMAIL = 'Your name'
DEFAULT_TO_EMAIL = 'Your email'
