from rest_framework import generics
from ..serializers import *
from ..models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class SpecialiteView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Specialite.objects.all()
    serializer_class = SpecialiteSerializer


class SpecialiteEditView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Specialite.objects.all()
    serializer_class = SpecialiteSerializer
    lookup_field = 'pk'
