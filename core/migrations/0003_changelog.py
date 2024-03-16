# Generated by Django 3.2.12 on 2024-03-16 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20240316_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('model_name', models.CharField(max_length=100)),
                ('object_id', models.PositiveIntegerField()),
                ('action', models.CharField(max_length=20)),
                ('details', models.TextField()),
                ('log_file', models.FileField(upload_to='change_logs/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
