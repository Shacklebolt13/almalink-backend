# Generated by Django 4.1.1 on 2022-11-30 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="skill",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
