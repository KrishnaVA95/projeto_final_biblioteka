from django.urls import path
from . import views


urlpatterns = [
    path("books/", views.BookView.as_view()),
    path("books/<int:pk>/", views.BookDetailView.as_view()),
    path("publishing_company/", views.PublishCompanyView.as_view()),
    path("publishing_company/<int:pk>/", views.PublishCompanyDetailView.as_view())
]