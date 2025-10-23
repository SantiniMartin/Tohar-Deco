from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass  # Solo usamos los campos que trae Django por defecto
