from .views import (
                    UserProfileViewSet, CityViewSet, HotelViewSet,
                    RoomsViewSet, BronViewSet, ReviewViewSet,
)

from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='user_list')
router.register(r'city', CityViewSet, basename='city_list')
router.register(r'hotel', HotelViewSet, basename='hotel_list')
router.register(r'room', RoomsViewSet, basename='room_list')
router.register(r'bron', BronViewSet, basename='bron_list')
router.register(r'review', ReviewViewSet, basename='review_list')


urlpatterns = [
    path('', include(router.urls)),
]
