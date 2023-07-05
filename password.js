import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qfs.settings")
import django
django.setup()

from django.contrib.auth.hashers import make_password

password = "password"

hashed_password = make_password(password)
print(hashed_password)
