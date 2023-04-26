from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.gis.geos import Point
from django.contrib.auth import get_user_model

User = get_user_model()


listing_type = (
    ('House', 'House'),
    ('Apartment', 'Apartment'),
    ('Office', 'Office'),
)

choices_property_status = (
    ('Sale', 'Sale'),
    ('Rent', 'Rent'),
)

choices_area = (
        ('Abuja', 'Abuja'),
        ('Outside Abuja', 'Outside Abuja'),
    )

choices_rental_frequency = (
        ('Month', 'Month'),
        ('Week', 'Week'),
        ('Day', 'Day'),
    )
class Listing(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(verbose_name=_('Title'), max_length=150)
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    area = models.CharField(verbose_name=_('Area'), max_length=20, blank=True, null=True, choices=choices_area)
    borough = models.CharField(verbose_name=_('Borough'), max_length=50, blank=True, null=True)
    listing_type = models.CharField(verbose_name=_('Listing Type'), max_length=50, choices=listing_type)
    price = models.DecimalField(verbose_name=_('Price'), max_digits=50, decimal_places=0)
    property_status = models.CharField(
        max_length=20, blank=True, null=True, choices=choices_property_status)
    rental_frequency = models.CharField(
        max_length=20, blank=True, null=True, choices=choices_rental_frequency)
    rooms = models.IntegerField(blank=True, null=True)
    furnished = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    cctv = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    picture1 = models.ImageField(
        blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    picture2 = models.ImageField(
        blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    picture3 = models.ImageField(
        blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    picture4 = models.ImageField(
        blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    picture5 = models.ImageField(
        blank=True, null=True, upload_to="pictures/%Y/%m/%d/")

    def __str__(self):
        return self.title

