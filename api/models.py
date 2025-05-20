from django.db import models
from users.models import User, Candidat, Admin
class Member(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    age = models.IntegerField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=50)
    start = models.DateField()

    def __str__(self):
        return self.title + " -> " + str(self.start)
    
class Region(models.Model):
    # Définir les choix
    REGION_CHOICES = [
        ('est', 'Est'),
        ('ouest', 'Ouest'),
        ('centre', 'Centre'),
    ]
    
    nom = models.CharField(
        max_length=20,
        choices=REGION_CHOICES,
        unique=True
    )

    def __str__(self):
        return self.get_nom_display()



# Modèle Compétence
class Competence(models.Model):
    nom = models.CharField(max_length=100)
    

# Modèle Domaine
class Domaine(models.Model):
    nom = models.CharField(max_length=100)


# Modèle Specialité
class Specialite(models.Model):
    nom = models.CharField(max_length=100)
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE, related_name="specialites")


# Modèle Langue
class Langue(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

# This is the bridge model
class CandidatLangue(models.Model):
    LEVEL_CHOICES = [
        ('A1', 'A1 - Débutant'),
        ('A2', 'A2 - Élémentaire'),
        ('B1', 'B1 - Intermédiaire'),
        ('B2', 'B2 - Intermédiaire supérieur'),
        ('C1', 'C1 - Avancé'),
        ('C2', 'C2 - Maîtrise'),
    ]

    candidat = models.ForeignKey(Candidat, on_delete=models.CASCADE)
    langue = models.ForeignKey(Langue, on_delete=models.CASCADE)
    niveau = models.CharField(max_length=2, choices=LEVEL_CHOICES)

    def __str__(self):
        return f"{self.candidat} - {self.langue} ({self.get_niveau_display()})"


# Modèle Offre d'emploi
class Offre(models.Model):
    id_offre = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100)
    description = models.TextField()
    competences = models.ManyToManyField('Competence')  
    date_creation = models.DateField(auto_now_add=True)
    admin = models.ForeignKey('Admin', on_delete=models.CASCADE, related_name='offres')
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True, blank=True)
    departement = models.ForeignKey('Departement', on_delete=models.SET_NULL, null=True, blank=True, related_name='offres')



# Modèle Candidature
class Candidature(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('accepte', 'Accepté'),
        ('refuse', 'Refusé'),
    ]
    candidat = models.ForeignKey('Candidat', on_delete=models.CASCADE)
    offre = models.ForeignKey('Offre', on_delete=models.CASCADE)
    date_postulation = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    date_entretien = models.DateTimeField(null=True, blank=True)  # Date d'entretien pour les candidats acceptés

# Modèle Formation
class Formation(models.Model):
    titre = models.CharField(max_length=200)
    etablissement = models.CharField(max_length=200)
    date_debut = models.DateField()
    date_fin = models.DateField()
    candidat = models.ForeignKey('Candidat', on_delete=models.CASCADE, related_name="formations")


# Modèle Expérience
class Experience(models.Model):
    entreprise = models.CharField(max_length=200)
    poste = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField()
    candidat = models.ForeignKey('Candidat', on_delete=models.CASCADE, related_name="experiences")


class Departement(models.Model):
     id_departement = models.AutoField(primary_key=True)
     nom_departement = models.CharField(max_length=100)

     def __str__(self):
        return self.nom_departement

class Entretien(models.Model):
    TYPE_ENTRETIEN_CHOICES = [
        ('video', 'Appel vidéo'),
        ('presentiel', 'Présentiel'),
    ]

    ETAT_CHOICES = [
        ('programme', 'Programmé'),
        ('complete', 'Complété'),
        ('annule', 'Annulé'),
    ]

    id_entretien = models.AutoField(primary_key=True)
    date_entretien = models.DateField()
    heure_entretien = models.TimeField()
    type_entretien = models.CharField(max_length=20, choices=TYPE_ENTRETIEN_CHOICES)
    etat = models.CharField(max_length=20, choices=ETAT_CHOICES, default='programme')
    candidature = models.ForeignKey('Candidature', on_delete=models.CASCADE)


    def __str__(self):
        return f"Entretien {self.id_entretien} - {self.type_entretien} le {self.date_entretien}"

