# Generated by Django 2.0.7 on 2018-07-23 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180722_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='location_10',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='location_4',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='location_5',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='location_6',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='location_7',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='location_8',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='location_9',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='location_1',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='location_2',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='location_3',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='sms_number',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
