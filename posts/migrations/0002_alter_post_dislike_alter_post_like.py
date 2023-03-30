# Generated by Django 4.1.7 on 2023-03-14 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_image_alter_profile_bio_and_more'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dislike',
            field=models.ManyToManyField(blank=True, related_name='Dislikes', to='user.profile', verbose_name='Beğenmeyenler'),
        ),
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='Likes', to='user.profile', verbose_name='Beğenenler'),
        ),
    ]
