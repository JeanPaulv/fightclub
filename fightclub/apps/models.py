from django.db import models
from django.contrib.auth.models import User, auth
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100,default='')
    ciudad = models.CharField(max_length=100, default='')
    twitter= models.URLField(default='')
    twitch= models.URLField(default='')
    perfil = models.ImageField(upload_to='imagen_perfil',blank=True)
    portada = models.ImageField(upload_to='imagen_portada', blank=True)


def create_profile(sender, **kwargs):
     if kwargs['created']:
         user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile ,sender=User)
    

