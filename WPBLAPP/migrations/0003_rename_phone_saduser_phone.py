# Generated by Django 4.2.1 on 2023-08-26 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("WPBLAPP", "0002_saduser"),
    ]

    operations = [
        migrations.RenameField(
            model_name="saduser", old_name="Phone", new_name="phone",
        ),
    ]