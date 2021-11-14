from rest_framework import serializers

from Experimental_API.models import Advisor,User,Booking

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ('Advisor_id', 'Advisor_name', 'Advisor_picture_url')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id','user_name','user_email','user_password')
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('Booking_id','Booking_time','user_id','Advisor_id')