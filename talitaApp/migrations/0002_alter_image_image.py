# Generated by Django 4.0.3 on 2022-04-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talitaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
