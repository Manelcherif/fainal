# Create your views here.

from rest_framework import generics
from ..serializers import *
from ..models import *
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
# CreateAPIView
# ListAPIView


class MemberView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [IsAuthenticated]
    queryset = Member.objects.all()
    serializer_class = MembersSerializer


class MemberEditView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [IsAuthenticated]
    queryset = Member.objects.all()
    serializer_class = MembersSerializer
    lookup_fields = ['pk']
