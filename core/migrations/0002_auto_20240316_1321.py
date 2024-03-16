# Generated by Django 3.2.12 on 2024-03-16 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agronomisttask',
            name='sample',
            field=models.OneToOneField(limit_choices_to={'analysttask__status': 'Complete'}, on_delete=django.db.models.deletion.CASCADE, related_name='agronomist_task', to='core.sample'),
        ),
        migrations.AlterField(
            model_name='labmanagertask',
            name='sample',
            field=models.OneToOneField(limit_choices_to={'agronomist_task__isnull': False}, on_delete=django.db.models.deletion.CASCADE, related_name='lab_manager_task', to='core.sample'),
        ),
    ]