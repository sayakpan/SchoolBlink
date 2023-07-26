# Generated by Django 4.1 on 2023-06-27 16:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Accounts", "0003_alter_user_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                error_messages={"unique": "A User with that email already exists."},
                max_length=200,
                unique=True,
                verbose_name="email Address",
            ),
        ),
    ]