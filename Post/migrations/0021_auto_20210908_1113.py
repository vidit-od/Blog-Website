# Generated by Django 3.2.5 on 2021-09-08 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0020_auto_20210908_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/catagory/'),
        ),
        migrations.AlterField(
            model_name='users',
            name='profile_pic',
            field=models.ImageField(default='static\\images\\profile_pic\\default-avatar.jpg', upload_to='images/profile_pic/'),
        ),
    ]
