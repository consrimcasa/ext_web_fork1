from django.urls import include, path
from . import views
from .views import*
app_name='adminapp'
urlpatterns=[
    path('',views.index,name='index'),
    path('articles/', views.articles, name='articles'),
    path('newPost/', views.newPost, name='newPost'),
    path('postes/', views.getPostes, name='postes'),
    path('annonces/', views.annonces, name='annonces'),
    path('newAnnoucement/', views.newAnnoucement, name='newAnnoucement'),
    path("users/", views.users, name="users"),
    # path('article_list', views.article_list, name='article_list'),
    
    # path('test/', views.test, name='test')
]