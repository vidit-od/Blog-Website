# Generated by Django 3.2.5 on 2021-09-03 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0015_auto_20210903_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
