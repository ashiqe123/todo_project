# Generated by Django 3.2.11 on 2022-03-02 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateField(default=1109),
            preserve_default=False,
        ),
    ]
