# Generated by Django 2.2.7 on 2020-04-06 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0004_quote_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_file',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote.Person'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote.Person'),
        ),
    ]
