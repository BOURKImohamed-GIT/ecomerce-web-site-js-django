# Generated by Django 3.1.4 on 2020-12-07 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_product_views_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='priceavant',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=7),
            preserve_default=False,
        ),
    ]
