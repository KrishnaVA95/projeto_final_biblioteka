from django.urls import path

from . import views

urlpatterns = [
    path("books/<int:book_pk>/copys/", views.CopyView.as_view()),
    path("books/<int:book_pk>/copys/<int:pk>/", views.CopyDetailView.as_view()),
]