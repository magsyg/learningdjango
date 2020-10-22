from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.db.models import Sum
from .managers import UserManager



class Section(models.Model):
    section_name =  models.CharField(unique=True, max_length=10, blank=False, null = False)
    def __str__(self):
        return self.section_name

    class Meta:
        verbose_name = _('section')
        verbose_name_plural = _('sections')

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=12, unique=True)

    section = models.ForeignKey(Section, null = True, default= None, on_delete=models.SET_NULL)

    objects = UserManager()
    is_staff = models.BooleanField(_('staff'), default=False)
    is_superuser = models.BooleanField(_('superuser'), default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    
    def distance_sum(self):
        return self.workouts.all().aggregate(Sum('distance'))['distance__sum'] or 0
    
    def score(self):
        return self.workouts.all().aggregate(Sum('score'))['score__sum']
        