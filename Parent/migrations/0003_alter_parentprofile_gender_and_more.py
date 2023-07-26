# Generated by Django 4.1 on 2023-07-14 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Profiles", "0021_alter_school_profiles_user"),
        ("Parent", "0002_parentprofile_city_parentprofile_country_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parentprofile",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("M", "Male"), ("F", "Female"), ("U", "Prefer Not to Say")],
                max_length=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="parentprofile",
            name="interested_class",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="SchoolClass",
                to="Profiles.schoolclass",
            ),
        ),
    ]