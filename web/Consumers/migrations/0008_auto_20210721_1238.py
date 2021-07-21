# Generated by Django 2.2 on 2021-07-21 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Consumers', '0007_consumer_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
