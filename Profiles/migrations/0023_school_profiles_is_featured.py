# Generated by Django 4.1 on 2023-07-15 09:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Profiles", "0022_alter_school_profiles_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="school_profiles",
            name="is_featured",
            field=models.BooleanField(default=False),
        ),
    ]