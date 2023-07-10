from django.urls import path
from .views import GenderView, GenderDetailView

urlpatterns = [
    path('genres/', GenderView.as_view()),
    path('genres/<int:pk>/', GenderDetailView.as_view()),
]