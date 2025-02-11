from rest_framework import serializers
from .models import (
                    UserProfile, City, Hotel, Rooms, RoomImages, Bron, Review,
)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImages
        fields = '__all__'


class BronSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bron
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
