# Generated by Django 2.2 on 2021-07-21 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Consumers', '0008_auto_20210721_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
