# Generated by Django 4.1 on 2023-07-05 13:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Profiles", "0004_alter_school_profiles_cover_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClassesPresent",
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
                ("rank", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="SchoolBoard",
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
                ("school_board", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="SchoolFormat",
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
                ("school_format", models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="SchoolType",
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
                ("school_type", models.CharField(max_length=15, unique=True)),
            ],
        ),
    ]
