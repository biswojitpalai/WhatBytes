from django.urls import path
from .views import MappingCreateListView, MappingByPatientView, MappingDeleteView

urlpatterns = [
    path('', MappingCreateListView.as_view()),                        # POST + GET /api/mappings/
    path('<int:patient_id>/', MappingByPatientView.as_view()),        # GET /api/mappings/<patient_id>/
    path('delete/<int:pk>/', MappingDeleteView.as_view()),            # DELETE /api/mappings/delete/<id>/
]
