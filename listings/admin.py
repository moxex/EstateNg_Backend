from django.contrib import admin
from listings.models import Listing
from .forms import ListingsForm


class ListingAdmin(admin.ModelAdmin):
    form = ListingsForm

# admin.site.register(Listing)
admin.site.register(Listing, ListingAdmin)
