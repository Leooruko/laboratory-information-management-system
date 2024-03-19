# Generated by Django 3.2.12 on 2024-03-18 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_changelog_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='stage',
            field=models.CharField(choices=[('registration', 'Registration stage'), ('analysis', 'Analysis stage'), ('recommendation', 'Recommendation stage'), ('processing', 'Processing stage')], default='registration', max_length=20),
        ),
    ]