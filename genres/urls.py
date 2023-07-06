from django.urls import path
from .views import GenreView, GenreDetailView

urlpatterns = [
    path('genres/', GenreView.as_view()),
    path('genres/<int:pk>/', GenreDetailView.as_view()),
]