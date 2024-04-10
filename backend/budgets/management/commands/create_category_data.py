from django.core.management.base import BaseCommand
from budgets.models import Category
import random

class Command(BaseCommand):
    help = 'Creates dummy data for the Category model'

    def handle(self, *args, **kwargs):
        categories = ['Food', 'Utilities', 'Transportation', 'Entertainment', 'Healthcare', 'Education']
        
        for name in categories:
            category = Category.objects.create(name=name)
            category.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully created Category: {category}'))
