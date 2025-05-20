from rest_framework import generics
from ..serializers import *
from ..models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class FormationView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Formation.objects.all()
    serializer_class = FormationSerializer


class FormationEditView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Formation.objects.all()
    serializer_class = FormationSerializer
    lookup_field = 'pk'
