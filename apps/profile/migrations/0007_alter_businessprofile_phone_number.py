# Generated by Django 4.1.5 on 2023-03-30 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0006_alter_employeeprofile_employer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessprofile',
            name='phone_number',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
