from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Category, Budget
from .serializers import CategorySerializer, BudgetSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
