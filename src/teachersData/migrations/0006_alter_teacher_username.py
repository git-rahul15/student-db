# Generated by Django 5.0.13 on 2025-04-10 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachersData', '0005_remove_teacher_teacher_id_teacher_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
