import os
from dotenv import load_dotenv
from envparse import env


load_dotenv()


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ['HOST'],
        'PORT': '5434',
        'NAME': 'checkpoint',
        'USER': 'guard',
        'PASSWORD': os.environ['PASSWORD'],
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = env.bool("DEBUG", default=False)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
