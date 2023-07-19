# Generated by Django 2.1.8 on 2023-06-10 05:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('OrderID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, max_length=30, null=True)),
                ('WhatsappNo', models.IntegerField(blank=True, null=True)),
                ('ContactNo', models.IntegerField(blank=True, null=True)),
                ('Address', models.CharField(max_length=250)),
                ('street_name', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('Courier', models.CharField(max_length=30)),
                ('TransactionId', models.CharField(blank=True, default=0, max_length=25, null=True)),
                ('TrackingId', models.CharField(blank=True, default=0, max_length=10, null=True)),
                ('No_Of_Items', models.IntegerField(blank=True, null=True)),
                ('item_color', models.CharField(blank=True, max_length=10, null=True)),
                ('item_size', models.CharField(blank=True, max_length=10, null=True)),
                ('file', models.FileField(upload_to='')),
                ('OrderStatus', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Production', 'Production'), ('Delivery', 'Delivery'), ('completed', 'completed')], default='pending', max_length=20)),
                ('Date', models.DateTimeField(default=datetime.datetime(2023, 6, 10, 5, 48, 58, 240109))),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterUsers',
            fields=[
                ('UserID', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
                ('EmailID', models.EmailField(max_length=254)),
                ('Phone', models.IntegerField(max_length=10)),
                ('Password', models.CharField(max_length=25)),
                ('Address', models.CharField(blank=True, max_length=255, null=True)),
                ('City', models.CharField(blank=True, max_length=25, null=True)),
                ('State', models.CharField(blank=True, max_length=25, null=True)),
                ('Zip', models.CharField(blank=True, default=0, max_length=10, null=True)),
                ('UserStatus', models.BooleanField(default=True)),
            ],
        ),
    ]
