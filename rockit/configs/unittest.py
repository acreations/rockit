import logging

from rockit.configs.default import *

NAME = "test-rockit"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '%s.sqlite3' % NAME),
    }
}

logging.disable(logging.CRITICAL)

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/tmp/noq-app-messages'