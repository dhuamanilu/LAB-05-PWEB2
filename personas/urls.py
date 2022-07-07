from django.urls import path
from personas.views import (PersonaListView,personasDeleteView,personaCreateVista,
                            personasShowObject)

app_name='personas'
urlpatterns=[
    path('',PersonaListView.as_view(),name='persona-list'),
    path('add/',personaCreateVista,name='adding'),
    path('<int:myID>/',personasShowObject,name='browsing'),
    path('<int:myID>/delete/',personasDeleteView,name='deleting'),
]