DEBUG = False
ALLOWED_HOSTS = ['*']

#settings for db on server
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db1',
        'USER': 'django_shop_admin',
        'PASSWORD': '$Password',
        'HOST': 'localhost',
        'PORT': '',                      # Set to empty string for default.
    }
}
