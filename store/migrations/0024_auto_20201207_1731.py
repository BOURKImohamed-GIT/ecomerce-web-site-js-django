# Generated by Django 3.1.4 on 2020-12-07 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_auto_20201207_1728'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
