from django.urls import path
from .views import ConstructionProjectView

urlpatterns = [
    path('construction-project/<slug_promp>/', ConstructionProjectView.as_view(), name='slug_promp'),
]
