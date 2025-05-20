from rest_framework import generics
from ..serializers import *
from ..models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class OffreView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer


class OffreEditView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer
    lookup_field = 'pk'
