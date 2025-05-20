from django.urls import path
from .views import *
urlpatterns = [
    # Member
    path('members/', MemberView.as_view(), name='member-list'),
    path('members/<int:pk>/', MemberEditView.as_view(), name='member-detail'),

    # Event
    path('events/', EventView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventEditView.as_view(), name='event-detail'),

    # Region
    path('regions/', RegionView.as_view(), name='region-list'),
    path('regions/<int:pk>/', RegionEditView.as_view(), name='region-detail'),

    # Competence
    path('competences/', CompetenceView.as_view(), name='competence-list'),
    path('competences/<int:pk>/', CompetenceEditView.as_view(), name='competence-detail'),

    # Domaine
    path('domaines/', DomaineView.as_view(), name='domaine-list'),
    path('domaines/<int:pk>/', DomaineEditView.as_view(), name='domaine-detail'),

    # Specialite
    path('specialites/', SpecialiteView.as_view(), name='specialite-list'),
    path('specialites/<int:pk>/', SpecialiteEditView.as_view(), name='specialite-detail'),

    # Langue
    path('langues/', LangueView.as_view(), name='langue-list'),
    path('langues/<int:pk>/', LangueEditView.as_view(), name='langue-detail'),

    # CandidatLangue
    path('candidatlangues/', CandidatLangueView.as_view(), name='candidatlangue-list'),
    path('candidatlangues/<int:pk>/', CandidatLangueEditView.as_view(), name='candidatlangue-detail'),

    # Offre
    path('offres/', OffreView.as_view(), name='offre-list'),
    path('offres/<int:pk>/', OffreEditView.as_view(), name='offre-detail'),

    # Candidature
    path('candidatures/', CandidatureView.as_view(), name='candidature-list'),
    path('candidatures/<int:pk>/', CandidatureEditView.as_view(), name='candidature-detail'),

    # Formation
    path('formations/', FormationView.as_view(), name='formation-list'),
    path('formations/<int:pk>/', FormationEditView.as_view(), name='formation-detail'),

    # Experience
    path('experiences/', ExperienceView.as_view(), name='experience-list'),
    path('experiences/<int:pk>/', ExperienceEditView.as_view(), name='experience-detail'),

    # Departement
    path('departements/', DepartementView.as_view(), name='departement-list'),
    path('departements/<int:pk>/', DepartementEditView.as_view(), name='departement-detail'),

    # Entretien
    path('entretiens/', EntretienView.as_view(), name='entretien-list'),
    path('entretiens/<int:pk>/', EntretienEditView.as_view(), name='entretien-detail'),
]
