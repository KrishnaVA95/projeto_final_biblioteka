from django.urls import path
from .views import LoanView, LoanDetailView, LoanDetailDestroyView, LoanDetailUpdateView

urlpatterns = [
    path('loans/', LoanView.as_view()),
    path('loans/<int:pk>/', LoanDetailView.as_view()),
    path('loans/<int:pk>/', LoanDetailDestroyView.as_view()),
    path('loans/<int:pk>/', LoanDetailUpdateView.as_view()),
]