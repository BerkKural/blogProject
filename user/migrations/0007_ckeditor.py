# Generated by Django 4.1.7 on 2023-03-28 11:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_profile_follow_alter_profile_followers'),
    ]

    operations = [
        migrations.CreateModel(
            name='ckEditor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
    ]