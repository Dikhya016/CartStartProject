# Generated by Django 5.0.2 on 2024-08-03 15:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_commerceApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to=settings.AUTH_USER_MODEL),
        ),
    ]
