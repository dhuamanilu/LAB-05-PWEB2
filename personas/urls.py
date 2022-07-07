from django.urls import path
from personas.views import (PersonaListView,PersonaDetailView,PersonaCreateView,PersonaUpdateView,
                            PersonaDeleteView,PersonaQueryView,PersonaQueryView2)

app_name='personas'
urlpatterns=[
    path('',PersonaListView.as_view(),name='persona-list'),
    path('create/',PersonaCreateView.as_view(),name='persona-create'),
    path('<int:pk>/',PersonaDetailView.as_view(),name='persona-detail'),
    path('<int:pk>/update/',PersonaUpdateView.as_view(),name='persona-update'),
    path('<int:pk>/delete/',PersonaDeleteView.as_view(),name='persona-delete'),
    path('query/',PersonaQueryView.as_view(),name='persona-query'),
    path('query2/',PersonaQueryView2.as_view(),name='persona-query2'),
]