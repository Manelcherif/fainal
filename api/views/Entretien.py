from rest_framework import generics
from ..serializers import *
from ..models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class EntretienView(generics.ListCreateAPIView):
    queryset = Entretien.objects.all()
    serializer_class = EntretienSerializer


class EntretienEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entretien.objects.all()
    serializer_class = EntretienSerializer
    lookup_field = 'pk'

