# Generated by Django 3.2 on 2021-06-20 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210615_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='friendly_name',
            field=models.CharField(default='product', max_length=254),
            preserve_default=False,
        ),
    ]