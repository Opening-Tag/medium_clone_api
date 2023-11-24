from .base import * #noqa
from .base import env
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY",default="AxZRsvL00q-2FRnNDPCWMMXQC2U3IlyeLMIvsjXCM4gB_EaTI40")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8000"]

# ALLOWED_HOSTS = []
