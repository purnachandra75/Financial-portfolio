# Generated by Django 5.1 on 2024-11-05 07:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usercradintials', '0003_userdetails_created_at_userdetails_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavingandGoals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_name', models.CharField(max_length=20)),
                ('target_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('current_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('deadline', models.DateField()),
                ('crated_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usercradintials.userdetails')),
            ],
        ),
    ]
