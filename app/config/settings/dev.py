#imports files or packages for this project
from config.settings.base import *


#imports librarys or package (python or django)
import os


DEBUG = True
ALLOWED_HOSTS = ['*']

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['POSTGRES_DB'],
        'USER': os.environ['POSTGRES_USER'],
        'HOST': os.environ['POSTGRES_HOST'],
        'PORT': os.environ['POSTGRES_PORT']
    },
}