# Generated by Django 4.2.1 on 2023-08-18 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("num", models.CharField(max_length=200)),
                ("name", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=10)),
                (
                    "totalamount",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "deposit",
                    models.DecimalField(decimal_places=2, max_digits=10, null=True),
                ),
                (
                    "withdraw",
                    models.DecimalField(decimal_places=2, max_digits=10, null=True),
                ),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "userid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="WPBLAPP.user"
                    ),
                ),
            ],
        ),
    ]