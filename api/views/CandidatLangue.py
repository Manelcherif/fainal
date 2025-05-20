from rest_framework import generics
from ..serializers import *
from ..models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CandidatLangueView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = CandidatLangue.objects.all()
    serializer_class = CandidatLangueSerializer


class CandidatLangueEditView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = CandidatLangue.objects.all()
    serializer_class = CandidatLangueSerializer
    lookup_field = 'pk'
