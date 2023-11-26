from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario') #lo jala del fields en el forms
    image = models.ImageField(default='default.jpg', upload_to='users/', verbose_name='Imagen de perfil')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Direccion')
    location = models.CharField(max_length=150, null=True, blank=True, verbose_name='Localidad')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Telefono')



    class Meta:
        verbose_name='perfil'
        verbose_name_plural = 'perfiles'
        ordering = ['-id']

    def __str__(self):
        return self.user.username
    

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    print("save_user_profile")
    instance.profile.save()



# Create your models here.
