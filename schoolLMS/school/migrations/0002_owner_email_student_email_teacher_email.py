# Generated by Django 4.0.8 on 2022-10-28 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="owner",
            name="email",
            field=models.EmailField(default=" ", max_length=100),
        ),
        migrations.AddField(
            model_name="student",
            name="email",
            field=models.EmailField(default=" ", max_length=100),
        ),
        migrations.AddField(
            model_name="teacher",
            name="email",
            field=models.EmailField(default=" ", max_length=100),
        ),
    ]
