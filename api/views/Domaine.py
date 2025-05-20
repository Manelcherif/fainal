from rest_framework import generics
from ..serializers import *
from ..models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class DomaineView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Domaine.objects.all()
    serializer_class = DomaineSerializer


class DomaineEditView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Domaine.objects.all()
    serializer_class = DomaineSerializer
    lookup_field = 'pk'
