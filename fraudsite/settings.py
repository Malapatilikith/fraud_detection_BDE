
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'test-secret'
DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = ['django.contrib.staticfiles','fraudapp']
MIDDLEWARE = ['django.middleware.common.CommonMiddleware']
ROOT_URLCONF = 'fraudsite.urls'
TEMPLATES = [{
    'BACKEND':'django.template.backends.django.DjangoTemplates',
    'DIRS':[BASE_DIR/'fraudapp'/'templates'],
    'APP_DIRS':True,
    'OPTIONS':{},
}]
WSGI_APPLICATION='fraudsite.wsgi.application'
STATIC_URL='/static/'
STATICFILES_DIRS=[BASE_DIR/'static']
