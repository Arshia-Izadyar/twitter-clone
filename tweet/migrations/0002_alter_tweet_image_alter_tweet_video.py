# Generated by Django 4.2 on 2023-10-09 06:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tweet", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tweet",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="./uploads", verbose_name="Image"),
        ),
        migrations.AlterField(
            model_name="tweet",
            name="video",
            field=models.FileField(blank=True, null=True, upload_to="./files", verbose_name="video"),
        ),
    ]
