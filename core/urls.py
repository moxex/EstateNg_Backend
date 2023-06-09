from django.contrib import admin
from django.urls import path, include
from listings.api import views as listings_api_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/listings/', listings_api_views.ListingList.as_view()),
    path('api/v1/listings/create/', listings_api_views.ListingCreate.as_view()),
    path('api/v1/listings/<int:pk>/', listings_api_views.ListingDetail.as_view()),
    path('api/v1/listings/<int:pk>/delete/',
         listings_api_views.ListingDelete.as_view()),
    path('apiv1/listings/<int:pk>/update/',
         listings_api_views.ListingUpdate.as_view()),

    path('api/v1-auth-djoser/', include('djoser.urls')),
    path('api/v1-auth-djoser/', include('djoser.urls.authtoken')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = 'EstateNG Admin'
admin.site.site_title = 'EstateNG Admin Portal'
admin.site.index_title = 'Welcome to the EstateNG Properties Portal'