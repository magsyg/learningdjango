from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=12, unique=True)
    SECTIONS = [
        ('SH', 'Shooter'),
        ('TR', 'Trooper'),
        ('PL', 'Pilot'),
        ('GR', 'General')
    ]
    section = models.CharField(_('section'),max_length=2, choices=SECTIONS, default='TR')
    
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['sections']
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

