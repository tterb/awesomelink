# Generated by Django 3.2.4 on 2021-06-19 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_auto_20210619_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awesomelink',
            name='normalized_url',
            field=models.CharField(max_length=900, unique=True),
        ),
    ]
