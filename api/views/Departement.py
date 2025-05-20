from rest_framework import generics
from ..serializers import *
from ..models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class DepartementView(generics.ListCreateAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer


class DepartementEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    lookup_field = 'pk'
