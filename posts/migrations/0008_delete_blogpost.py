# Generated by Django 4.1.7 on 2023-03-28 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_blogpost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
