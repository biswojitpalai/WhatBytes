from django.urls import path
from .views import MappingCreateListView, MappingByPatientView, MappingDeleteView

urlpatterns = [
    path('', MappingCreateListView.as_view()),                        
    path('<int:patient_id>/', MappingByPatientView.as_view()),        
    path('delete/<int:pk>/', MappingDeleteView.as_view()),           
]
