from django.db import models

# Create your models here.

options =[
    [0, 'Presencial'],
    [1, 'On Line']
]

class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    lastname = models.CharField(max_length=50, verbose_name='Apellido')
    email = models.EmailField(verbose_name='Correo Electrónico')
    message = models.TextField(verbose_name='Mensaje')
    gender = models.CharField(max_length=50, verbose_name='Género')
    nacionality = models.CharField(max_length=50, verbose_name='Nacionalidad')
    profession = models.CharField(max_length=50, verbose_name='Profesión')
    status = models.CharField(max_length=50, verbose_name='Estado Civil')
    childs = models.CharField(max_length=50, verbose_name='Cantidad Hijos')
    sport = models.CharField(max_length=50, verbose_name='Deporte Preferido')
    music = models.CharField(max_length=50, verbose_name='Tipo de Música')
    food = models.CharField(max_length=50, verbose_name='Tipo de Comida')
    drink = models.CharField(max_length=50, verbose_name='Tipo de Bebida')
    contact_type = models.IntegerField(choices=options, verbose_name='Tipo de Contacto')
    subscription = models.BooleanField(default=False, verbose_name='Suscribirme a Correos Informativos')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Envío')
