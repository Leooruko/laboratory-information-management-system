# Generated by Django 3.2.12 on 2024-04-07 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_chemical_sample'),
    ]

    operations = [
        migrations.AlterField(
            model_name='full',
            name='sample',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.sample'),
        ),
        migrations.AlterField(
            model_name='microbio',
            name='sample',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.sample'),
        ),
    ]
