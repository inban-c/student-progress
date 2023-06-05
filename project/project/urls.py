"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
     path('home',views.home),
    path('faculty',views.faculty),
    path('facultypage',views.facultypage),
    path('studentpage/<str:reg>',views.studentpage),
    path('signup',views.signup),
    path('stdsignup',views.stdsignup),
    path('stdlogin',views.stdlogin),
    path('student',views.student),
    path('facsignup',views.facsignup),
    path('fsignup',views.fsignup),
    path('Ssignup',views.Ssignup),
    path('csbs',views.csbs),
    path('csbs2',views.csbs2),
    path('csbs3',views.csbs3),
    path('cia1/<str:reg>',views.cia1),
    path('cia2/<str:reg>',views.cia2),
    path('cia3/<str:reg>',views.cia3),
    path('ia2',views.ia2),
    path('ia3',views.ia3),
    path('facultyfront',views.facultyfront),
    path('progress/<str:reg>',views.progress),
    #path('ViewResult/<str:dept>',views.Vresult),
    ]