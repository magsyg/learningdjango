from django.db import models
from users.models import User
from django.utils import timezone


class Trening(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank=False, verbose_name="Bruker")
    NOTHING = 0
    STRENGTH = 1
    RUNNING = 2
    CYCLING = 3
    WALKING = 4
    SWIMMING = 5
    SKIING = 6
    TYPES = [
        (NOTHING, '-------'),
        (STRENGTH, 'Styrke'),
        (RUNNING, 'Løping'),
        (CYCLING, 'Sykling'),
        (WALKING, 'Gåing'),
        (SWIMMING, 'Svømming'),
        (SKIING, 'Ski')
    ]
    POINTS = {
        NOTHING: 0,
        STRENGTH: 4,
        RUNNING: 1,
        CYCLING: 1/4,
        WALKING: 1/2,
        SWIMMING: 2,
        SKIING: 1/2,
    }
    type = models.IntegerField(choices=TYPES, default=0, verbose_name="Treningstype", blank=False, null = False)
    distance = models.FloatField(null=True, blank=True, verbose_name="Distanse")
    comment = models.TextField(null=True, blank=True, verbose_name="Kommentar")

    date = models.DateField(null=True, blank=True, verbose_name="Dato")
    created = models.DateTimeField(null=True, blank=True, editable=False, verbose_name="Opprettet")

    class Meta:
        ordering = ["-id"]
        verbose_name = "Treningsøkt"
        verbose_name_plural = "Treningsøkter"

    
    def __str__(self):
        return f"{self.user}, {self.get_type_display()} ({self.distance} km), {self.date}"

    def give_points(self):
        p = 0
        if self.type == Trening.STRENGTH:
            p = Trening.POINTS[self.type]
        elif self.distance:
            p = self.distance * Trening.POINTS[self.type]
        return round(p, 1)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()

        return super(type(self), self).save(*args, **kwargs)


    @classmethod
    def NOTHING_P(cls):
        return cls.POINTS[cls.NOTHING]

    @classmethod
    def STRENGTH_P(cls):
        return cls.POINTS[cls.STRENGTH]

    @classmethod
    def RUNNING_P(cls):
        return cls.POINTS[cls.RUNNING]

    @classmethod
    def CYCLING_P(cls):
        return cls.POINTS[cls.CYCLING]

    @classmethod
    def WALKING_P(cls):
        return cls.POINTS[cls.WALKING]

    @classmethod
    def SWIMMING_P(cls):
        return cls.POINTS[cls.SWIMMING]

    @classmethod
    def SKIING_P(cls):
        return cls.POINTS[cls.SKIING]