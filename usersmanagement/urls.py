from django.urls import include, path
from . import views
from .views import*
app_name='usersmanagement'
urlpatterns=[
    # path('', include('adminapp.urls', namespace='adminapp')),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('create/', views.create_user, name='create'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('update_password/<str:user_id>', views.update_password, name='update_password'),
    path('update_user/<str:user_id>', views.update_user, name='update_user'),
    path('delete_user/<str:user_id>', views.delete_user, name='delete_user'),
]