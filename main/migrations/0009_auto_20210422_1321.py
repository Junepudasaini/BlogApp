# Generated by Django 3.1.4 on 2021-04-22 07:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210422_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_upload',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 22, 13, 21, 46, 475583), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='post',
            name='intro',
            field=models.CharField(max_length=2555),
        ),
    ]
