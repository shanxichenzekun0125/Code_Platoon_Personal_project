from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    
    # you can't run admin page with this
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
   



    # You can run admin page and create superuser properly
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']
