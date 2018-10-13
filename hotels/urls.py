from . import views
from django.urls import path

urlpatterns = [
    path('providers', views.Providers.as_view()),
    path('AvailableHotel', views.AvailableHotel.as_view()),
    path('AvailableHotel/<int:hotel_id>/Amenity', views.HotelAmenity.as_view()),
    path('BestHotel', views.BestHotel.as_view()),
    path('CrazyHotel', views.CrazyHotel.as_view()),
]
