# Generated by Django 5.1.3 on 2024-11-11 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login_page", "0005_member_name_member_password_alter_member_id"),
    ]

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
                ("username", models.CharField(max_length=150, unique=True)),
                ("password", models.CharField(max_length=128)),
                ("name", models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name="Member",
        ),
    ]
