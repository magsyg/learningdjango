from django.db import models
from users.models import User
from django.utils import timezone
from datetime import date

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank=False, verbose_name="Bruker")
    
    EMPTY = 0
    SKI = 1
    LOPE = 2
    SVOMMING = 3
    STYRKE = 4

    TYPES = [   
        (EMPTY, '--------'),
        (SKI, 'Ski'),
        (LOPE,'Løpe'),
        (SVOMMING, 'Svømming'),
        (STYRKE, 'Styrke')
    ]

    treningtype = models.IntegerField(choices=TYPES, default=EMPTY, verbose_name="Treningstype")
    distance = models.FloatField(blank=True, null = True, verbose_name="Distanse")
    date = models.DateField(default=date.today, verbose_name="Dato")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created")

    class Meta:
        verbose_name = 'workout'
        verbose_name_plural = 'workouts'