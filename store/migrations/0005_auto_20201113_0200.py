# Generated by Django 3.1.2 on 2020-11-13 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20201105_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date_orderd',
            new_name='date_ordered',
        ),
    ]