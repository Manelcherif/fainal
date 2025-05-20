from rest_framework import generics
from ..serializers import *
from ..models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CompetenceView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer


class CompetenceEditView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer
    lookup_field = 'pk'
