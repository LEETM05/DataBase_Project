# Generated by Django 5.1.3 on 2024-11-11 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login_page", "0003_rename_login_member"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="id",
            field=models.CharField(
                default="", max_length=20, primary_key=True, serialize=False
            ),
        ),
    ]
