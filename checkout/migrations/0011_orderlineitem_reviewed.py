# Generated by Django 3.2 on 2021-06-15 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_remove_orderlineitem_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='reviewed',
            field=models.BooleanField(default=False),
        ),
    ]