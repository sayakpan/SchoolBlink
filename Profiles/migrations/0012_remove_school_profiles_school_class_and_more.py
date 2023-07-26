# Generated by Django 4.1 on 2023-07-06 05:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Profiles", "0011_alter_schoolclass_rank_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="school_profiles",
            name="school_class",
        ),
        migrations.AddField(
            model_name="school_profiles",
            name="school_class",
            field=models.ManyToManyField(blank=True, to="Profiles.schoolclass"),
        ),
    ]
