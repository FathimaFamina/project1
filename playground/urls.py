"""
URL configuration for playground project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from poll import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),


    
    path('persons/', views.persons,name='persons'),
    path('addperson/', views.addperson,name='addperson'),
    path('addpersoncreate/', views.addpersoncreate,name='addpersoncreate'),




    path('persons/perdetails/<int:id>/', views.perdetails,name='perdetails'),
    path('persons/perdetails/<int:id>/deleteperson/', views.deleteperson,name='deleteperson'),
    path('persons/perdetails/<int:id>/update/', views.update,name='update'),
    path('updateperson/<int:id>/', views.updateperson,name='updateperson'),


    path('test/', views.test,name='test'),

    path('', views.main),

    path('ffn/', views.ffn,name='ffn'),
    path('fln/', views.fln,name='fln'),
    path('fc/', views.fc,name='fc'),



]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)