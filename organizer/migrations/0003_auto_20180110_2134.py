# Generated by Django 2.0 on 2018-01-10 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0002_auto_20180109_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='done_flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='done_flag',
            field=models.BooleanField(default=False),
        ),
    ]