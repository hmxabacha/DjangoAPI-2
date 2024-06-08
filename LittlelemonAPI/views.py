from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle

class MenuItemView(generics.ListCreateAPIView):
    throttle_classes=[AnonRateThrottle,UserRateThrottle]
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer
    
    
class SingleMenuItem(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset=MenuItem
    serializer_class=MenuItemSerializer