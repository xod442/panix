import os
#
SECRET_KEY = 'you-will-never-guess'
DEBUG=True
MONGODB_DB = 'panix'
HOSTNAME = 'https://127.0.0.1'
UPLOAD_FOLDER = '/app/static/'
STATIC_IMAGE_URL = 'images'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')
APP_TEMPLATE = os.path.join(APP_ROOT, 'templates')
