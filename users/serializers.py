from django.contrib.auth.models import Group
from rest_framework import serializers
from users.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """

    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name',
                  'password', 'is_active', 'last_login', 'start_date')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.is_active = True
        instance.is_admin = True
        instance.save()

        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get(
            'username', instance.username)
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.is_active = validated_data.get(
            'is_active', instance.is_active)
        if password is not None:
            instance.set_password(password)
        groups = validated_data.pop('groups', instance.groups)
        instance.save()
        return instance
class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Admin
        fields = ['id', 'user', 'nom_admin', 'prenom', 'date_naissance',
                  'adresse', 'telephone', 'region']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['role'] = 'admin'
        user = UserSerializer().create(user_data)
        admin = Admin.objects.create(user=user, **validated_data)
        return admin

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            UserSerializer().update(instance.user, user_data)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    
class CandidatSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Candidat
        fields = ['id', 'user', 'nom', 'prenom', 'sexe', 'date_naissance',
                  'telephone', 'profession', 'description', 'competences',
                  'specialite', 'region', 'photo_profil']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['role'] = 'candidat'
        user = UserSerializer().create(user_data)
        candidat = Candidat.objects.create(user=user, **validated_data)
        return candidat

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            UserSerializer().update(instance.user, user_data)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        if user.is_admin:
            token = super().get_token(user)
            return token
