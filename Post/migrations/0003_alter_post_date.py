# Generated by Django 3.2.5 on 2021-08-17 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_auto_20210812_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.CharField(max_length=50),
        ),
    ]