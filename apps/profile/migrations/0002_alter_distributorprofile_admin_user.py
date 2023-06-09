# Generated by Django 4.1.5 on 2023-02-26 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("profile", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="distributorprofile",
            name="admin_user",
            field=models.OneToOneField(
                limit_choices_to={"type": "DISTRIBUTOR"},
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="admin_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
