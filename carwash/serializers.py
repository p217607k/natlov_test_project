from rest_framework import serializers
from .models import *

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'user', 'model', 'license_plate', 'vehicle_type', 'is_active']
        read_only_fields = ['id']

    def validate_license_plate(self, value):
        """
        Custom validation to ensure the license plate is unique.
        """
        if Car.objects.filter(license_plate=value).exists():
            raise serializers.ValidationError("This license plate already exists.")
        return value
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'price']
        read_only_fields = ['id']

    def validate_price(self, value):
        
        if value <= 0:
            raise serializers.ValidationError("The price must be greater than zero.")
        return value

class OrderSerializer(serializers.ModelSerializer):
    car_details = serializers.StringRelatedField(source='car', read_only=True)
    service_details = serializers.StringRelatedField(source='service', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'car', 'car_details', 'service', 'service_details', 'order_date', 'is_completed']
        read_only_fields = ['id', 'order_date']

    def validate(self, data):
        
        if data['car'].vehicle_type == '2W' and data['service'].name.lower().startswith('4w'):
            raise serializers.ValidationError("Selected service is not compatible with the vehicle type.")
        return data
class WorkLogSerializer(serializers.ModelSerializer):
    order_details = serializers.StringRelatedField(source='order', read_only=True)

    class Meta:
        model = WorkLog
        fields = ['id', 'order', 'order_details', 'performed_at', 'completed']
        read_only_fields = ['id', 'performed_at']

    def validate(self, data):
        
        if data.get('completed') and not data['order'].is_completed:
            raise serializers.ValidationError("Work cannot be marked completed until the order is marked completed.")
        return data
    
class PaymentSerializer(serializers.ModelSerializer):
    order_details = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = ['id', 'order', 'order_details', 'amount_paid', 'payment_date', 'is_successful']
        read_only_fields = ['id', 'payment_date']

    def get_order_details(self, obj):
        """
        Return a nested representation of the order details.
        """
        return {
            "car_model": obj.order.car.model,
            "service_name": obj.order.service.name,
            "order_date": obj.order.order_date
        }

    def validate_amount_paid(self, value):
        """
        Validate that the amount paid is positive.
        """
        if value <= 0:
            raise serializers.ValidationError("Amount paid must be a positive value.")
        return value
class ReviewSerializer(serializers.ModelSerializer):
    order_details = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'order', 'order_details', 'rating', 'comment']
        read_only_fields = ['id']

    def get_order_details(self, obj):
        
        return {
            "car_model": obj.order.car.model,
            "service_name": obj.order.service.name,
            "order_date": obj.order.order_date
        }

    def validate_rating(self, value):
        """
        Validate that the rating is between 1 and 5.
        """
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value



class LicenseSerializer(serializers.ModelSerializer):
    car_details = serializers.SerializerMethodField()

    class Meta:
        model = License
        fields = ['id', 'car', 'car_details', 'license_type', 'expiry_date']
        read_only_fields = ['id']

    def get_car_details(self, obj):
        """
        Return details of the associated car.
        """
        return {
            "car_model": obj.car.model,
            "license_plate": obj.car.license_plate,
            "vehicle_type": obj.car.vehicle_type,
        }

    def validate_expiry_date(self, value):
        """
        Ensure the expiry date is not in the past.
        """
        from datetime import date
        if value < date.today():
            raise serializers.ValidationError("The expiry date cannot be in the past.")
        return value
    
class WarrantySerializer(serializers.ModelSerializer):
    car_details = serializers.SerializerMethodField()

    class Meta:
        model = Warranty
        fields = ['id', 'car', 'car_details', 'warranty_period', 'coverage']
        read_only_fields = ['id']

    def get_car_details(self, obj):
        """
        Returns details of the associated car.
        """
        return {
            "car_model": obj.car.model,
            "license_plate": obj.car.license_plate,
            "vehicle_type": obj.car.vehicle_type,
        }

    def validate_warranty_period(self, value):
        """
        Ensure the warranty period is a reasonable duration.
        """
        if value <= 0:
            raise serializers.ValidationError("Warranty period must be greater than zero.")
        return value
    
class AppointmentSerializer(serializers.ModelSerializer):
    car_details = serializers.SerializerMethodField()
    service_details = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = ['id', 'car', 'car_details', 'service', 'service_details', 'appointment_time', 'is_confirmed']
        read_only_fields = ['id']

    def get_car_details(self, obj):
        """
        Returns the car details for the appointment.
        """
        return {
            "car_model": obj.car.model,
            "license_plate": obj.car.license_plate,
            "vehicle_type": obj.car.vehicle_type,
        }

    def get_service_details(self, obj):
        """
        Returns the service details for the appointment.
        """
        return {
            "service_name": obj.service.name,
            "price": obj.service.price,
            "description": obj.service.description,
        }

    def validate_appointment_time(self, value):
        """
        Validates that the appointment time is in the future.
        """
        from django.utils.timezone import now
        if value <= now():
            raise serializers.ValidationError("Appointment time must be in the future.")
        return value
    
class CarClinicSerializer(serializers.ModelSerializer):
    car_details = serializers.SerializerMethodField()
    service_details = serializers.SerializerMethodField()

    class Meta:
        model = CarClinic
        fields = ['id', 'car', 'car_details', 'service', 'service_details', 'visit_date', 'is_completed']
        read_only_fields = ['id', 'visit_date']

    def get_car_details(self, obj):
        """
        Return detailed information about the car.
        """
        return {
            "car_model": obj.car.model,
            "license_plate": obj.car.license_plate,
            "vehicle_type": obj.car.vehicle_type,
        }

    def get_service_details(self, obj):
        """
        Return detailed information about the service.
        """
        return {
            "service_name": obj.service.name,
            "price": obj.service.price,
            "description": obj.service.description,
        }