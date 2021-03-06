# Generated by Django 3.2.8 on 2021-11-02 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_task_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name_plural': 'TodoLists'},
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('NotCompleted', 'Not Completed'), ('Completed', 'Completed')], default='NotCompleted', max_length=20),
        ),
    ]
