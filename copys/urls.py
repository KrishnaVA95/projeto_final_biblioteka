from django.urls import path

from . import views
from copys import views as copys_views

urlpatterns = [
    path("copys/", views.CopyView.as_view()),
    path("copys/<int:pk>/", copys_views.CopyDetailView.as_view()),
]