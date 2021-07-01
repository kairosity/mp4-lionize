# Generated by Django 3.2 on 2021-07-01 13:38

from django.db import migrations, models
import lionize.validations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20210616_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_last_name',
            field=models.CharField(blank=True, max_length=60, null=True, validators=[lionize.validations.validate_min_length_2]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[lionize.validations.validate_phone_number, lionize.validations.validate_min_length_5_phone]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='facebook_handle',
            field=models.CharField(blank=True, max_length=40, null=True, validators=[lionize.validations.validate_handle]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='instagram_handle',
            field=models.CharField(blank=True, max_length=40, null=True, validators=[lionize.validations.validate_handle]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='twitter_handle',
            field=models.CharField(blank=True, max_length=40, null=True, validators=[lionize.validations.validate_handle]),
        ),
    ]
