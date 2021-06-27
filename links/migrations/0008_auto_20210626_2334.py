# Generated by Django 3.2.4 on 2021-06-26 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0007_alter_awesomelink_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='awesomelink',
            name='rating',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='awesomelink',
            name='rating_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
