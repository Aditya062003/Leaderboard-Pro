# Generated by Django 3.2.4 on 2023-06-02 14:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeforcesuser',
            name='last_activity',
            field=models.BigIntegerField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)),
        ),
        migrations.AlterField(
            model_name='codeforcesuserratingupdate',
            name='timestamp',
            field=models.BigIntegerField(default=0),
        ),
    ]
