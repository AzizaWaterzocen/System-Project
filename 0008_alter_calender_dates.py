# Generated by Django 5.0.6 on 2024-05-21 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_alter_calender_dates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calender',
            name='dates',
            field=models.DateField(),
        ),
    ]
