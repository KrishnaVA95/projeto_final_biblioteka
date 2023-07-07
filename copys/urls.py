from django.urls import path

from . import views

urlpatterns = [
    path("books/<int:pk>/copys/", views.CopyCreateView.as_view()),
    path("books/copys/", views.CopyListView.as_view()),
    path("books/copys/<int:pk>/", views.CopyDetailView.as_view()),
]