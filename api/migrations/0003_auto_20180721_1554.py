# Generated by Django 2.0.7 on 2018-07-21 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180721_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='sms_number',
            new_name='device_number',
        ),
        migrations.AddField(
            model_name='user',
            name='radius',
            field=models.FloatField(default=5),
        ),
    ]