from django.urls import path
from .views import *
urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('', ExpenseListCreateAPIView.as_view(), name='expense-list'),
    path('<int:pk>/', ExpenseDetailAPIView.as_view(), name='expense-detail'),
    ]