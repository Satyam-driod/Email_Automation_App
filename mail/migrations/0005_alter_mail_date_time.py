# Generated by Django 3.2.11 on 2022-01-07 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0004_alter_mail_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 7, 12, 48, 11, 829955)),
        ),
    ]
