# Generated by Django 4.1.2 on 2022-10-28 12:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0005_remove_calenderpost_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task_member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calenderpost',
            name='members',
            field=models.ManyToManyField(through='task_member.TaskMember', to=settings.AUTH_USER_MODEL),
        ),
    ]