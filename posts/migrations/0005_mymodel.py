# Generated by Django 4.1.7 on 2023-03-28 11:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
    ]