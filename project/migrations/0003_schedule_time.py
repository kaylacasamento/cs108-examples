# Generated by Django 2.2.7 on 2020-04-27 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='time',
            field=models.TextField(blank=True),
        ),
    ]
