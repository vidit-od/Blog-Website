# Generated by Django 3.2.5 on 2021-09-03 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0013_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(blank=True, choices=[('Female', 'female'), ('others', 'Others'), ('male', 'male')], max_length=20),
        ),
    ]
