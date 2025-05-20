from rest_framework import generics
from ..serializers import *
from ..models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class LangueView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Langue.objects.all()
    serializer_class = LangueSerializer


class LangueEditView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Langue.objects.all()
    serializer_class = LangueSerializer
    lookup_field = 'pk'