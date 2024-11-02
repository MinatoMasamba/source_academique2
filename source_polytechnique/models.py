from django.db import models
from django.utils import timezone
# Create your models here.

from django.contrib.auth.models import User

# Définir les promotions
PROMOTION_CHOICES = [
    ('L1', 'Licence 1'),
    ('PREPA', 'Préparatoire'),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    promotion = models.CharField(max_length=100,choices=PROMOTION_CHOICES)  # Par exemple, 'L1' ou 'PREPA'
    first_name = models.CharField(max_length=30, blank=True, null=True)  # Assurez-vous que ces champs existent
    last_name = models.CharField(max_length=30, blank=True, null=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    numero_whatsapp = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Message(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Cours(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    maman = models.FileField(upload_to='cours/', blank=True, null=True)
    promotion = models.CharField(max_length=5, choices=PROMOTION_CHOICES)
    date_ajout = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Cours"
        verbose_name_plural = "Cours"

    def __str__(self):
        return self.titre

class Interro(models.Model):
    titre = models.CharField(max_length=200)
    fichier = models.FileField(upload_to='interros/')
    promotion = models.CharField(max_length=5, choices=PROMOTION_CHOICES)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_donnee = models.DateField(default=timezone.now)  # Champ pour la date précise où le TP a été donné

    def __str__(self):
        return self.titre

class Examen(models.Model):
    titre = models.CharField(max_length=200)
    fichier = models.FileField(upload_to='examens/')
    promotion = models.CharField(max_length=5, choices=PROMOTION_CHOICES)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_donnee = models.DateField(default=timezone.now)  # Champ pour la date précise où le TP a été donné

    def __str__(self):
        return self.titre

class TP(models.Model):
    titre = models.CharField(max_length=200)
    fichier = models.FileField(upload_to='tp/')
    promotion = models.CharField(max_length=5, choices=PROMOTION_CHOICES)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_donnee = models.DateField(default=timezone.now)  # Champ pour la date précise où le TP a été donné

    def __str__(self):
        return self.titre

class Note(models.Model):
    titre = models.CharField(max_length=200)
    fichier = models.FileField(upload_to='notes/')
    promotion = models.CharField(max_length=5, choices=PROMOTION_CHOICES)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()









from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Create your models here.
