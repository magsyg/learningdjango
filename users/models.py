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
    score = models.IntegerField(_('score'), default=0)
    
    objects = UserManager()
    is_staff = models.BooleanField(_('staff'), default=False)
    is_superuser = models.BooleanField(_('superuser'), default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
