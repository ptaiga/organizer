# Generated by Django 2.0 on 2018-06-06 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0011_task_repeat'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='snooze_date',
            field=models.DateTimeField(default=None, null=True, verbose_name='date snoozed'),
        ),
    ]
