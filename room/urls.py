
from .views import (
    UserProfileListAPIView, UserProfileEditAPIView, CityListAPIView, CityDetailAPIView, HotelListAPIView, HotelDetailAPIView,
    RoomsListAPIView, RoomsDetailAPIView, BronViewSet, ReviewCreateAPIView,
)

from django.urls import path, include
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'bron', BronViewSet, basename='bron_list')



urlpatterns = [
    path('', include(router.urls)),

    path('users/', UserProfileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileEditAPIView.as_view(), name='user_edit'),

    path('hotel/', HotelListAPIView.as_view(), name='hotel_list'),
    path('hotel/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),

    path('city/', CityListAPIView.as_view(), name='city_list'),
    path('city/<int:pk>/', CityDetailAPIView.as_view(), name='city_detail'),

    path('room/', RoomsListAPIView.as_view(), name='room_list'),
    path('room/<int:pk>/', RoomsDetailAPIView.as_view(), name='room_detail'),

    path('review/', ReviewCreateAPIView.as_view(), name='review_list'),

]
