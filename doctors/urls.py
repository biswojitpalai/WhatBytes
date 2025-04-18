from django.urls import path
from .views import DoctorCreateListView, DoctorDetailView

urlpatterns = [
    path('', DoctorCreateListView.as_view()),       
    path('<int:pk>/', DoctorDetailView.as_view()),  
]
