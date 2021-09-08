# Generated by Django 3.2.5 on 2021-09-08 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0019_auto_20210905_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(blank=True, choices=[('Female', 'female'), ('male', 'male'), ('others', 'Others')], default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
