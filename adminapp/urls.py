from django.urls import include, path
from . import views
from .views import*
app_name='adminapp'
urlpatterns=[
    path('',views.index,name='index'),
    path('articles/', views.articles, name='articles'),
    path('newPost/', views.newPost, name='newPost'),
    path('postes/', views.getPostes, name='postes'),
    path("users/", views.users, name="users"),
    # path('article_list', views.article_list, name='article_list'),
    path('consulate_contacts/', views.consulate_contacts, name='consulate_contacts'),
    path('newConsulate_contact/', views.newConsulate_contact, name='newConsulate_contact'),
    path('delete_consulate_contact/<str:consulate_contact_id>', views.delete_consulate_contact, name='delete_consulate_contact'),
    # path('test/', views.test, name='test')
    path('etat_civils/', views.etat_civils, name='etat_civils'),
    path('newetat_civil/', views.newetat_civil, name='newetat_civil'),
    path('update_etat_civil/<str:etat_civil_id>', views.update_etat_civil, name='update_etat_civil'),
    path('delete_etat_civil/<str:etat_civil_id>', views.delete_etat_civil, name='delete_etat_civil'),
    ##########
    path('visa_infos/', views.visa_infos, name='visa_infos'),
    path('newvisa_info/', views.newvisa_info, name='newvisa_info'),
    path('update_visa_info/<str:visa_info_id>', views.update_visa_info, name='update_visa_info'),
    path('delete_visa_info/<str:visa_info_id>', views.delete_visa_info, name='delete_visa_info'),
]