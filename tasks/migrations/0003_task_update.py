# Generated by Django 3.2.8 on 2021-10-28 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20211028_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
