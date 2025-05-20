# Create your views here.

from rest_framework import generics
from ..serializers import *
from ..models import *
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
# CreateAPIView
# ListAPIView


class EventView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventEditView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_fields = ['pk']
