# Generated by Django 3.2.5 on 2021-09-01 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0007_comment_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]