from django.urls import path
from .views import *

urlpatterns = [
    path('account/', AccountsView.as_view()),
    path('account/<int:pk>', EditAccountView.as_view()),

    path('groups/', GroupsView.as_view()),

    path('login/', UserLogin.as_view()),
    path('login/test/', TestLogin.as_view()),

    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
     # Candidat views
    path('candidats/', CandidatListCreateView.as_view(), name='candidat-list-create'),
    path('candidats/<int:pk>/', CandidatDetailView.as_view(), name='candidat-detail'),

    # Admin views
    path('admins/', AdminListCreateView.as_view(), name='admin-list-create'),
    path('admins/<int:pk>/', AdminDetailView.as_view(), name='admin-detail'),

    # Profile endpoints
    path('profile/candidat/', CandidatProfileView.as_view(), name='candidat-profile'),
    path('profile/admin/', AdminProfileView.as_view(), name='admin-profile'),     

]
