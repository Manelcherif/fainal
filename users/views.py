
from users.models import *
from users.serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import Group
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)


class AccountsView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.filter(is_admin=True)
        return queryset


class EditAccountView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    lookup_fields = ['pk']
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupsView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = GroupsSerializer
    queryset = Group.objects.all()


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer


class TestLogin(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        print(serializer.data)
        return Response(serializer.data)
    
class CandidatListCreateView(generics.ListCreateAPIView):
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer
    permission_classes = [IsAdminUser]  # Only admins can view/add candidats

class CandidatDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer
    permission_classes = [IsAdminUser]  # Only admins can modify candidats
    lookup_field = 'pk'
class CandidatProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = CandidatSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Candidat.objects.get(user=self.request.user)
    
class AdminListCreateView(generics.ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAdminUser]  # You can add custom permission later

class AdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'
class AdminProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Admin.objects.get(email_admin=self.request.user.email)    

