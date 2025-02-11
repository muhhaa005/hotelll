from .models import (UserProfile, City, Hotel, Rooms, Bron, Review)
from rest_framework import viewsets, generics
from .serializers import (
                        UserProfileSerializer, CityListSerializer, CityDetailSerializer,  HotelListSerializer, HotelDetailSerializer,
                        RoomsListSerializer, RoomsDetailSerializer, BronSerializer, ReviewSerializer
)

class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class UserProfileEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class CityListAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializer

class CityDetailAPIView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializer


class HotelListAPIView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer

class HotelDetailAPIView(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer


class RoomsListAPIView(generics.ListAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsListSerializer

class RoomsDetailAPIView(generics.RetrieveAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsDetailSerializer



class BronViewSet(viewsets.ModelViewSet):
    queryset = Bron.objects.all()
    serializer_class = BronSerializer


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



