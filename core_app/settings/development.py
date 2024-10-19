from .base import *


DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuraciones adicionales para desarrollo
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Email settings para depuración
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Configuración de archivos estáticos para desarrollo
STATICFILES_DIRS = [BASE_DIR / 'static']