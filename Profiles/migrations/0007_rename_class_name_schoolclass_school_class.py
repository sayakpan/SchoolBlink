# Generated by Django 4.1 on 2023-07-05 17:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Profiles", "0006_schoolclass_delete_classespresent_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="schoolclass",
            old_name="class_name",
            new_name="school_class",
        ),
    ]