# Generated by Django 3.2.7 on 2023-04-26 21:03

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('area', models.CharField(blank=True, choices=[('Abuja', 'Abuja'), ('Outside Abuja', 'Outside Abujas')], max_length=20, null=True, verbose_name='Area')),
                ('borough', models.CharField(blank=True, max_length=50, null=True, verbose_name='Borough')),
                ('listing_type', models.CharField(choices=[('House', 'House'), ('Apartment', 'Apartment'), ('Office', 'Office')], max_length=50, verbose_name='Listing Type')),
                ('price', models.DecimalField(decimal_places=0, max_digits=50, verbose_name='Price')),
                ('property_status', models.CharField(blank=True, choices=[('Sale', 'Sale'), ('Rent', 'Rent')], max_length=20, null=True)),
                ('rental_frequency', models.CharField(blank=True, choices=[('Month', 'Month'), ('Week', 'Week'), ('Day', 'Day')], max_length=20, null=True)),
                ('rooms', models.IntegerField(blank=True, null=True)),
                ('furnished', models.BooleanField(default=False)),
                ('pool', models.BooleanField(default=False)),
                ('elevator', models.BooleanField(default=False)),
                ('cctv', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326, verbose_name='Location')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('picture1', models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/')),
                ('picture2', models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/')),
                ('picture3', models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/')),
                ('picture4', models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/')),
                ('picture5', models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/')),
            ],
        ),
    ]
