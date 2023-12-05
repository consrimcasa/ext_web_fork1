"""minister_ext URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    # path('i18n/', include('django.conf.urls.i18n')),
    # path('admin/', admin.site.urls),
    # path('admin/', include('usersmanagement.urls', namespace='usersmanagement')),
    
    path('admin/', include('adminapp.urls', namespace='adminapp')),
    path('usersmanagement/', include('usersmanagement.urls', namespace='usersmanagement')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('', include('app1.urls', namespace='app1')),
    # path('adminapp/', include('adminapp.urls', namespace='adminapp')),
    # path('tinymce/', include('tinymce.urls')),
)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)





# urlpatterns = i18n_patterns(
#     path('hello/', your_view),
#     # ... more views here ...
# )
