import uuid
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class ProfileUsersApp(models.model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    hammers = models.PositiveIntegerField(default=3)
    premium_active = models.BooleanField(default=False)
    date_expired_supcription = models.DateTimeField(null=True, blank=True)
    date_created_supcription = models.DateTimeField(null=True, blank=True)
    advertisements = models.BooleanField(default=True)

    def __str__(self):
        return f"Perfil de {self.user.email}"
    


class Hammer(models.model):
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    consumers = models.PositiveIntegerField(default=0)
    limit = models.PositiveIntegerField(default=3)
    create_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Martillos consumidos: {self.consumers} / {self.limit}"
    
