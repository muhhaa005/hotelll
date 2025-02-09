from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(City)
admin.site.register(Hotel)
admin.site.register(Rooms)
admin.site.register(RoomImages)
admin.site.register(Bron)
admin.site.register(Review)

