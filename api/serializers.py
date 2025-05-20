from rest_framework import serializers
from .models import *

class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"

class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = "__all__"

class DomaineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domaine
        fields = "__all__"

class SpecialiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialite
        fields = "__all__"

class LangueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Langue
        fields = "__all__"

class CandidatLangueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidatLangue
        fields = "__all__"

class OffreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offre
        fields = "__all__"

class CandidatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidature
        fields = "__all__"

class FormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formation
        fields = "__all__"

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = "__all__"

class EntretienSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entretien
        fields = "__all__"
