# Generated by Django 3.1.4 on 2020-12-07 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_auto_20201207_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]