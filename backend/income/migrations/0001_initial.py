# Generated by Django 5.0.4 on 2024-04-10 15:08

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=50)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('choices', models.CharField(choices=[('stock', 'Stock'), ('buisness', 'Buisness'), ('paycheck', 'Paycheck'), ('rd', 'Recurring Deposit'), ('mf', 'Mutual funds')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
