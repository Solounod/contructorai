from django.urls import path
from .views import ConstructionProjectView, TypeProyectViewList, ProyectDetailView

urlpatterns = [
    path('construction-project/<slug_promp>/', ConstructionProjectView.as_view(), name='slug_promp'),
    path('construction-projectlist/', TypeProyectViewList.as_view(), name='list_proyect'),
    path('construction-project-detail/<slug_promp>/', ProyectDetailView.as_view(), name='list_proyect'),

]
