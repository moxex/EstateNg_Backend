from django.contrib import admin
from listings.models import Listing
# from .forms import ListingsForm


class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'area', 'listing_type', 'seller', 'price', 'property_status']
    list_filter = ['title', 'area', 'listing_type' ]
    list_display_links = ['title', 'seller', 'listing_type']
#     form = ListingsForm

# admin.site.register(Listing)
admin.site.register(Listing, ListingAdmin)
