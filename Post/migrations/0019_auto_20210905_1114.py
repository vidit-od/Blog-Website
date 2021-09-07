# Generated by Django 3.2.5 on 2021-09-05 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0018_auto_20210903_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(related_name='blog_likes', to='Post.users'),
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'male'), ('Female', 'female'), ('others', 'Others')], max_length=20),
        ),
        migrations.DeleteModel(
            name='likes',
        ),
    ]