# Generated by Django 4.2.3 on 2023-08-15 20:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("studentreg", "0007_modulefeedback_instructorfeedback"),
    ]

    operations = [
        migrations.DeleteModel(
            name="InstructorFeedback",
        ),
    ]