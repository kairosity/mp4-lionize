# Generated by Django 3.2 on 2021-06-26 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_friendly_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_shop',
            field=models.BooleanField(default=True),
        ),
    ]