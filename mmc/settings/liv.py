from .base import *  # noqa

CACHE_REDIS_DATABASE = '2'
CACHES['default']['LOCATION'] = '127.0.0.1:6379:' + CACHE_REDIS_DATABASE

INTERNAL_IPS = INTERNAL_IPS + ('', )
ALLOWED_HOSTS = ['mmc.cch.kcl.ac.uk', 'mmc.kdl.kcl.ac.uk']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'app_mmc_liv',
        'USER': 'app_mmc',
        'PASSWORD': '',
        'HOST': ''
    },
}


# -----------------------------------------------------------------------------
# Local settings
# -----------------------------------------------------------------------------

try:
    from .local import *  # noqa
except ImportError:
    pass
