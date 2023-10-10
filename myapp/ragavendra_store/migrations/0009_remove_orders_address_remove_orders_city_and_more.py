# Generated by Django 4.1.2 on 2023-09-01 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ragavendra_store', '0008_alter_orders_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='city',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='state',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='street_name',
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='state',
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='orders',
            name='Area_name',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='District',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='Dono',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='orders',
            name='LandMark',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='orders',
            name='Mandal',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='Village',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user_info',
            name='Area_name',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user_info',
            name='District',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user_info',
            name='Dono',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='user_info',
            name='LandMark',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='user_info',
            name='Mandal',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user_info',
            name='Postal_code',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user_info',
            name='Village',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='ContactNo',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 1, 16, 13, 13, 673443)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='WhatsappNo',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='phonenumber',
            field=models.BigIntegerField(),
        ),
        migrations.AddField(
            model_name='orders',
            name='Postal_code',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='State',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user_info',
            name='State',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]