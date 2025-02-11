from .models import (UserProfile, City, Hotel, Rooms, Bron, Review)
from rest_framework import viewsets
from .serializers import (
                        UserProfileSerializer, CitySerializer, HotelSerializer,
                        RoomsSerializer, BronSerializer, ReviewSerializer
)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer


class BronViewSet(viewsets.ModelViewSet):
    queryset = Bron.objects.all()
    serializer_class = BronSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

