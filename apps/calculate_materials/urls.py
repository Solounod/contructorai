from django.urls import path
from .views import ConstructionProjectView

urlpatterns = [
    path('construction-project/', ConstructionProjectView.as_view(), name='construction_project'),
]
