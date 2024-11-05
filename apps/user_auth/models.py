from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import timedelta


class ProfileUsersApp(AbstractUser):
    hammers = models.PositiveIntegerField(verbose_name="Martillos",default=3)
    premium_active = models.BooleanField(verbose_name="Premium",default=False)
    date_expired_supcription = models.DateTimeField(verbose_name="Fecha expiracion",null=True, blank=True)
    date_created_supcription = models.DateTimeField(verbose_name="Fecha de supcripcion",null=True, blank=True)
    advertisements = models.BooleanField(verbose_name="Anuncios",default=True)
    limit_proyect = models.PositiveBigIntegerField(verbose_name="Limite de proyectos",default=4)

    def __str__(self):
        return f"Profile {self.user.email}"
    

    class Meta:
        ordering = ['-id']
        verbose_name = 'user'
        verbose_name_plural = verbose_name


    def activate_premium(self, duration_days= 30):
        self.premium_active = True
        self.date_created_supcription = timezone.now()
        self.date_expired_supcription = timezone.now() + timedelta(days=duration_days)
        self.hammers += 200
        self.limit_proyect += 200
        self.advertisements = False
        self.save()

    def deactivate_premium(self):
        self.premium_active = False
        self.date_expired_subscription = None
        self.date_created_subscription = None
        self.hammers = 3  
        self.limit_project = 4
        self.advertisements = True
        self.save()

    