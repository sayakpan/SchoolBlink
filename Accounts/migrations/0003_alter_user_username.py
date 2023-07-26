# Generated by Django 4.1 on 2023-06-27 16:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Accounts", "0002_user_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                error_messages={"unique": "A user with that username already exists."},
                help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                max_length=150,
                unique=True,
            ),
        ),
    ]