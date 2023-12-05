from django.urls import path
from . import views
from .views import*
app_name='stock'
urlpatterns=[
    path('',views.home,name='home'),
    path('consulate/', views.consulate, name='consulate'),
    path('services/', views.services, name='services'),
    path('affaires_sociales/', views.affaires_sociales, name='affaires_sociales'),
    path('services_etrangers/', views.services_etrangers, name='services_etrangers'),
    path('documents_citoyens/', views.documents_citoyens, name='documents_citoyens'),
    path('etat_civil/', views.etat_civil, name='etat_civil'),
    path('announcements/', views.announcements, name='announcements'),
    path('gallery/', views.gallery, name='gallery'),
    path("immatriculation/", views.immatriculation, name="immatriculation"),
    path('studentsInfo/', views.studentsInfo, name='studentsInfo'),
    path('visas/', views.visas, name='visas'),
    path('fonctions_du_consulat/', views.fonctions_du_consulat, name='fonctions_du_consulat'),
    path('contact/', views.contact, name='contact'),
    
    
    path('details_page/<str:post_id>', view=details_page, name='details_page'),
    path('annoucement_details/<str:annonce_id>', view=annoucement_details, name='annoucement_details'),
    
    path('cv/', view=cv, name='cv'),
    path('bienvenu/', view=bienvenu, name='bienvenu')
    
]