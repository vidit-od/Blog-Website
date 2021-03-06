# Generated by Django 3.2.5 on 2021-09-12 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0025_auto_20210912_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='atagory/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='catagory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Post.catagory'),
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'male'), ('Female', 'female'), ('others', 'Others')], default=None, max_length=20, null=True),
        ),
    ]
