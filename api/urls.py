from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', GetDashboardData.as_view()),

    path('member/', MemberView.as_view()),
    path('member/<int:pk>', MemberEditView.as_view()),

    path('event/', EventView.as_view()),
    path('event/<int:pk>', EventEditView.as_view()),
]
