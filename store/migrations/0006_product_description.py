# Generated by Django 3.1.2 on 2020-11-15 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20201113_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
