# Generated by Django 4.2.1 on 2023-08-28 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("WPBLAPP", "0004_saduser_date_user_date_user_year"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="date",),
        migrations.RemoveField(model_name="user", name="year",),
    ]