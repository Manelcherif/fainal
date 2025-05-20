from rest_framework import generics
from ..serializers import *
from ..models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class RegionView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionEditView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    lookup_field = 'pk'
