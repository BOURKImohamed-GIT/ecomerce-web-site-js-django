# Generated by Django 3.1.2 on 2020-11-15 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20201115_0228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='imagesee',
            new_name='see',
        ),
    ]
