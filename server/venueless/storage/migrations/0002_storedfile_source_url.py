# Generated by Django 3.0.9 on 2020-08-22 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("storage", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="storedfile",
            name="source_url",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
