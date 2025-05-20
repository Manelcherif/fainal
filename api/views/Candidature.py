from rest_framework import generics
from ..serializers import *
from ..models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CandidatureView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer


class CandidatureEditView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer
    lookup_field = 'pk'
