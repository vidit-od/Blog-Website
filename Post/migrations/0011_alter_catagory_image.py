# Generated by Django 3.2.5 on 2021-09-01 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0010_alter_catagory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/catagory/'),
        ),
    ]
