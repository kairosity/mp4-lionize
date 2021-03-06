# Generated by Django 3.2 on 2021-06-16 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_message_resolved'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_first_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_last_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='consultation',
            field=models.BooleanField(default=False),
        ),
    ]
