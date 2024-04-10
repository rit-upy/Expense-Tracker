from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from expenses.models import Expense
from budgets.models import Category
import random
from faker import Faker
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Creates dummy data for the Expense model'

    def handle(self, *args, **kwargs):
        fake = Faker()
        users = User.objects.all()
        categories = Category.objects.all()
        
        for _ in range(100):
            user = User.objects.get(id=1)
            category = random.choice(categories)
            amount = round(random.uniform(10.00, 1000.00), 2)
            description = fake.text()
            date = fake.date_time_between(start_date="-1y", end_date="now")
            expense = Expense.objects.create(
                user=user,
                category=category,
                amount=amount,
                description=description,
                date=date
            )
            expense.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully created Expense: {expense}'))
