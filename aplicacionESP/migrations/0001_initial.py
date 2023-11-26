# Generated by Django 4.2.7 on 2023-11-15 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='users/', verbose_name='Imagen de perfil')),
                ('address', models.CharField(blank=True, max_length=150, null=True, verbose_name='Direccion')),
                ('location', models.CharField(blank=True, max_length=150, null=True, verbose_name='Localidad')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefono')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'perfil',
                'verbose_name_plural': 'perfiles',
                'ordering': ['-id'],
            },
        ),
    ]
