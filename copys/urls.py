from django.urls import path

from . import views
from copys import views as copys_views

urlpatterns = [
    path("books/<int:book_pk>/copys/", views.CopyView.as_view()),
    path("books/<int:book_pk>/copys/<int:pk>/", copys_views.CopyDetailView.as_view()),
]