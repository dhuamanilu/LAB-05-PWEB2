from django.urls import path
from personas.views import (personasDeleteView,personaCreateVista,
                            personasShowObject, personasListView)

app_name='personas'
urlpatterns=[
    path('add/',personaCreateVista,name='adding'),
    path('<int:myID>/',personasShowObject,name='browsing'),
    path('<int:myID>/delete/',personasDeleteView,name='deleting'),
    path('',personasListView,name='listing'),
]