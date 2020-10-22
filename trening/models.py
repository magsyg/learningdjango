from django.db import models
from users.models import User
from django.utils import timezone
from datetime import date

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank=False, verbose_name="Bruker", related_name="workouts")
    
    EMPTY = "non"
    SKI = "ski"
    LOPE = "lop"
    SVOMMING = "svm"
    STYRKE = "sty"

    TYPES = [   
        (EMPTY, '--------'),
        (SKI, 'Ski'),
        (LOPE,'Løpe'),
        (SVOMMING, 'Svømming'),
        (STYRKE, 'Styrke')
    ]
    M_DATA = {
        EMPTY: (0,0,'--------'),
        SKI: (0,1, 'Ski'),
        LOPE: (0,1, 'Løpe'),
        SVOMMING: (0, 2, 'Svømming'),
        STYRKE: (1.5, 0, 'Styrke')
    }
    score = models.FloatField(default=0, verbose_name="Score")
    treningtype = models.CharField(choices=TYPES, max_length=3, default=EMPTY, verbose_name="Treningstype")
    distance = models.FloatField(blank=True, null = True, default = 0, verbose_name="Distanse")
    date = models.DateField(default=date.today, verbose_name="Dato")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created")

    def __str__(self):
        if(self.treningtype == 0 or self.treningtype == 4):
            return (self.M_DATA[self.treningtype][2]+", "+str(self.date)+" "+str(self.score))
        else: 
             return (self.M_DATA[self.treningtype][2]+" "+str(self.distance)+"km, "+str(self.date)+" "+str(self.score))
        
    def save(self, *args, **kwargs):
        self.score = self.M_DATA[self.treningtype][0]+self.M_DATA[self.treningtype][1]*self.distance
        super(Workout, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'workout'
        verbose_name_plural = 'workouts'



