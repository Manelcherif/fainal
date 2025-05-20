from rest_framework import generics
from ..serializers import *
from ..models import *
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView


# CreateAPIView
# ListAPIView


class GetDashboardData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        members_count = Member.objects.count()
        events_count = Event.objects.count()

        response = {
            "members_count": members_count,
            "events_count": events_count,
        }
        return Response(response)
