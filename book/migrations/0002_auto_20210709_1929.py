# Generated by Django 3.1 on 2021-07-09 17:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publishDate',
            field=models.DateField(default=datetime.datetime(2021, 7, 9, 17, 29, 36, 584753, tzinfo=utc)),
        ),
    ]
