# Generated by Django 3.2 on 2021-06-14 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_orderlineitem_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='user_profile',
        ),
    ]
