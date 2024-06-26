# Generated by Django 5.0.2 on 2024-05-25 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="InstrumentType",
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
                ("instrument_type_name", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Mixer",
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
                ("instrument_name", models.CharField(max_length=500)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("last_used", models.DateTimeField(auto_now=True)),
                ("max_speed", models.IntegerField()),
                ("min_speed", models.IntegerField()),
                (
                    "instrument_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="landing_pages.instrumenttype",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Oven",
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
                ("instrument_name", models.CharField(max_length=500)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("last_used", models.DateTimeField(auto_now=True)),
                ("max_temp", models.IntegerField()),
                ("max_dim_W", models.IntegerField()),
                ("max_dim_L", models.IntegerField()),
                ("max_dim_H", models.IntegerField()),
                ("max_capacity", models.IntegerField()),
                (
                    "instrument_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="landing_pages.instrumenttype",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
