# Generated by Django 3.1.4 on 2021-04-20 07:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210420_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_upload',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 20, 13, 15, 42, 672635), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]