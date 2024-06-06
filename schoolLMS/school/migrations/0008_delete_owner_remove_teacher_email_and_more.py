# Generated by Django 4.0.8 on 2022-12-01 11:11

import uuid

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0007_rename_teacherexperties_teacherexperty_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Owner",
        ),
        migrations.RemoveField(
            model_name="teacher",
            name="email",
        ),
        migrations.AlterField(
            model_name="student",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, region=None, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, region=None, unique=True
            ),
        ),
    ]