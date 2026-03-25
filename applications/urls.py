from django.urls import path
from .views import ApplicationListCreateView, ApplicationDetailView

urlpatterns = [
    path('applications/', ApplicationListCreateView.as_view()),
    path('applications/<int:pk>/', ApplicationDetailView.as_view()),
]