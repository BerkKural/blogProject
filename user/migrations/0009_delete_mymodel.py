# Generated by Django 4.1.7 on 2023-03-28 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_rename_ckeditor_mymodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
