from django.shortcuts import render
from rest_framework import viewsets

from Experimental_API.serializers import AdvisorSerializer, UserSerializer,BookingSerializer
from Experimental_API.models import Advisor,User,Booking

# Create your views here.
class AdvisorViewSet(viewsets.ModelViewSet):
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer