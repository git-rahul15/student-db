# Generated by Django 5.0.11 on 2025-03-31 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsData', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(auto_created=True, max_length=50, unique=True),
        ),
    ]
