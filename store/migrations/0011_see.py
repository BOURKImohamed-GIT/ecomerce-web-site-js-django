# Generated by Django 3.1.2 on 2020-11-22 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_product_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='See',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('simage', models.ImageField(blank=True, null=True, upload_to='')),
                ('sdescription', models.CharField(max_length=400, null=True)),
            ],
        ),
    ]