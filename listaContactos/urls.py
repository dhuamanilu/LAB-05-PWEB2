"""listaContactos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from inicio.views import myHomeView, anotherView, vistaCreada, otraView
from personas.views import personaTestView, personaCreateView, searchForHelp, personasAnotherCreateView , personaCreateVista
urlpatterns = [
    path('',myHomeView,name='Página de inicio'),
    path('observar/',vistaCreada),
    path('another/',anotherView),
    path('admin/', admin.site.urls),
    path('otra/',otraView),
    path('persona/',personaTestView,name='Otro'),
    path('add/',personaCreateVista,name='crear persona '),
    path('anotherAdd/',personasAnotherCreateView,name='OtroAgregarPersonas'),
    path('agregar/',personaCreateView,name='createPersona'),
    path('search/',searchForHelp,name='buscar'),
]
