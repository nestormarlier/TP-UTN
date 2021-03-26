from django.contrib.auth.models import AbstractUser

from django.db import models

class User(AbstractUser):

    # imagen = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank= True)
    CATEGORIA_CHOICES = [
        ('SUPERVISOR', 'SUPERVISOR'),
        ('MAQUINISTA', 'MAQUINISTA'),
        ('1ER AYUDANTE', '1ER AYUDANTE'),
        ('2DO AYUDANTE', '2DO AYUDANTE'),
        ('MECANICO', 'MECÁNICO'),
    ]

    categoria = models.TextField(choices=CATEGORIA_CHOICES)