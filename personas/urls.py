from django.urls import path
from personas.views import (PersonaListView,PersonaDetailView,personaCreateVista,
                            personasDeleteView)

app_name='personas'
urlpatterns=[
    path('',PersonaListView.as_view(),name='persona-list'),
    path('add/',personaCreateVista,name='adding'),
    path('<int:pk>/',PersonaDetailView.as_view(),name='persona-detail'),
    path('<int:myID>/delete/',personasDeleteView,name='deleting'),
]