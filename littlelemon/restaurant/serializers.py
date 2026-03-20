from rest_framework import serializers
from .models import Menu, Booking


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

# class BookingSerializer(serializers.ModelSerializer):
#     BookingDate = serializers.DateTimeField(
#         input_formats=['%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M:%S'],
#         required=True
#     )

#     class Meta:
#         model = Booking
#         fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    # BookingDate = serializers.CharField()

    class Meta:
        model = Booking
        fields = '__all__'