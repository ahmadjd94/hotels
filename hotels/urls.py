from . import views
from django.urls import path

urlpatterns = [
    path('providers', views.Providers.as_view()),
    path('providers/<int:provider_id>/hotels', views.HotelView.as_view()),
    path('hotels/<int:hotel_id>/amenity', views.HotelAmenity.as_view()),
    path('AvailableHotel', views.AvailableHotel.as_view()),
    path('BestHotel', views.BestHotel.as_view()),
    path('CrazyHotel', views.CrazyHotel.as_view()),
]
