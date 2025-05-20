from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, Group, PermissionsMixin, BaseUserManager
from api.models import Competence, Specialite, Region


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_admin', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(**other_fields)

    def create_user(self, password, **other_fields):

        user = self.model(**other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('candidat', 'Candidat'),
    ) 
    username = models.CharField(max_length=150, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='candidat')
    email = models.EmailField()
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    start_date = models.DateTimeField(default=timezone.now)

    objects = CustomAccountManager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
class Admin(AbstractBaseUser, PermissionsMixin):
    email_admin = models.EmailField(_('email address'), unique=True)
    nom_admin = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, default='')
    date_naissance = models.DateField(null=True, blank=True)
    adresse = models.CharField(max_length=100, default='')
    telephone = models.CharField(max_length=20, default='0000000000')
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    last_login = None
       
    objects = CustomAccountManager()
    
    USERNAME_FIELD = 'email_admin'
    REQUIRED_FIELDS = ['nom_admin', 'prenom']
    
    def __str__(self):
        return f"{self.nom_admin} {self.prenom} ({self.email_admin})"

class Candidat(AbstractBaseUser, PermissionsMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(_('email address'), unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=10)
    date_naissance = models.DateField()
    telephone = models.CharField(max_length=20)
    profession = models.CharField(max_length=100)
    description = models.TextField()
    competences = models.ManyToManyField(Competence)
    specialite = models.ManyToManyField(Specialite)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    photo_profil = models.ImageField(upload_to='profile_photos/', default='profile_photos/default.jpg', blank=True, null=True)
    last_login = None
    objects = CustomAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom', 'date_naissance']
    
   
    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.email})"    