# Generated by Django 4.0.3 on 2022-05-19 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talitaApp', '0003_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images'),
        ),
    ]
