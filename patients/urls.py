from django.urls import path
from .views import PatientCreateListView, PatientDetailView

urlpatterns = [
    path('', PatientCreateListView.as_view()),               
    path('<int:pk>/', PatientDetailView.as_view()),          
]
