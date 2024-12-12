from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Car
from .serializers import *

class CarListCreateAPIView(APIView):
    """
    Handles GET and POST requests for the Car model.
    """
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarDetailAPIView(APIView):
    """
    Handles GET, PUT, PATCH, and DELETE requests for individual Car instances.
    """
    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return None

    def get(self, request, pk):
        car = self.get_object(pk)
        if not car:
            return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        car = self.get_object(pk)
        if not car:
            return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        car = self.get_object(pk)
        if not car:
            return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarSerializer(car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        car = self.get_object(pk)
        if not car:
            return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
        car.delete()
        return Response({"message": "Car deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
class ServiceListCreateAPIView(APIView):
    """
    Handles GET and POST requests for the Service model.
    """
    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ServiceDetailAPIView(APIView):
    
    def get_object(self, pk):
        try:
            return Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            return None

    def get(self, request, pk):
        service = self.get_object(pk)
        if not service:
            return Response({"error": "Service not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ServiceSerializer(service)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        service = self.get_object(pk)
        if not service:
            return Response({"error": "Service not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        service = self.get_object(pk)
        if not service:
            return Response({"error": "Service not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ServiceSerializer(service, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        service = self.get_object(pk)
        if not service:
            return Response({"error": "Service not found"}, status=status.HTTP_404_NOT_FOUND)
        service.delete()
        return Response({"message": "Service deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    

class OrderListCreateAPIView(APIView):
    """
    Handles GET and POST requests for Order.
    """
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailAPIView(APIView):
    """
    Handles GET, PUT, PATCH, and DELETE requests for individual orders.
    """
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return None

    def get(self, request, pk):
        order = self.get_object(pk)
        if not order:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        order = self.get_object(pk)
        if not order:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = self.get_object(pk)
        if not order:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)
        order.delete()
        return Response({"message": "Order deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
class WorkLogListCreateAPIView(APIView):
    """
    Handles GET and POST requests for WorkLogs.
    """
    def get(self, request):
        work_logs = WorkLog.objects.all()
        serializer = WorkLogSerializer(work_logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WorkLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class WorkLogDetailAPIView(APIView):
    """
    Handles GET, PUT, PATCH, and DELETE requests for a single WorkLog.
    """
    def get_object(self, pk):
        try:
            return WorkLog.objects.get(pk=pk)
        except WorkLog.DoesNotExist:
            return None

    def get(self, request, pk):
        work_log = self.get_object(pk)
        if not work_log:
            return Response({"error": "Work Log not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WorkLogSerializer(work_log)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        work_log = self.get_object(pk)
        if not work_log:
            return Response({"error": "Work Log not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WorkLogSerializer(work_log, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        work_log = self.get_object(pk)
        if not work_log:
            return Response({"error": "Work Log not found"}, status=status.HTTP_404_NOT_FOUND)
        work_log.delete()
        return Response({"message": "Work Log deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class PaymentListCreateAPIView(APIView):
    """
    Handles GET and POST requests for Payments.
    """
    def get(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PaymentDetailAPIView(APIView):
    """
    Handles GET, PUT, PATCH, and DELETE requests for a single Payment.
    """
    def get_object(self, pk):
        try:
            return Payment.objects.get(pk=pk)
        except Payment.DoesNotExist:
            return None

    def get(self, request, pk):
        payment = self.get_object(pk)
        if not payment:
            return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        payment = self.get_object(pk)
        if not payment:
            return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        payment = self.get_object(pk)
        if not payment:
            return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)
        payment.delete()
        return Response({"message": "Payment deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class ReviewListCreateAPIView(APIView):
    """
    Handles GET and POST requests for Reviews.
    """
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ReviewDetailAPIView(APIView):
    """
    Handles GET, PUT, PATCH, and DELETE requests for a single Review.
    """
    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return None

    def get(self, request, pk):
        review = self.get_object(pk)
        if not review:
            return Response({"error": "Review not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        review = self.get_object(pk)
        if not review:
            return Response({"error": "Review not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        review = self.get_object(pk)
        if not review:
            return Response({"error": "Review not found"}, status=status.HTTP_404_NOT_FOUND)
        review.delete()
        return Response({"message": "Review deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class LicenseListCreateAPIView(APIView):
    """
    Handles GET and POST requests for Licenses.
    """
    def get(self, request):
        licenses = License.objects.all()
        serializer = LicenseSerializer(licenses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LicenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LicenseDetailAPIView(APIView):
    """
    Handles GET, PUT, PATCH, and DELETE requests for a single License.
    """
    def get_object(self, pk):
        try:
            return License.objects.get(pk=pk)
        except License.DoesNotExist:
            return None

    def get(self, request, pk):
        license = self.get_object(pk)
        if not license:
            return Response({"error": "License not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = LicenseSerializer(license)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        license = self.get_object(pk)
        if not license:
            return Response({"error": "License not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = LicenseSerializer(license, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        license = self.get_object(pk)
        if not license:
            return Response({"error": "License not found"}, status=status.HTTP_404_NOT_FOUND)
        license.delete()
        return Response({"message": "License deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    


class WarrantyListCreateAPIView(APIView):
    """
    Handles GET and POST requests for Warranties.
    """
    def get(self, request):
        warranties = Warranty.objects.all()
        serializer = WarrantySerializer(warranties, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WarrantySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WarrantyDetailAPIView(APIView):
    """
    Handles GET, PUT, PATCH, and DELETE requests for a single Warranty.
    """
    def get_object(self, pk):
        try:
            return Warranty.objects.get(pk=pk)
        except Warranty.DoesNotExist:
            return None

    def get(self, request, pk):
        warranty = self.get_object(pk)
        if not warranty:
            return Response({"error": "Warranty not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WarrantySerializer(warranty)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        warranty = self.get_object(pk)
        if not warranty:
            return Response({"error": "Warranty not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WarrantySerializer(warranty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        warranty = self.get_object(pk)
        if not warranty:
            return Response({"error": "Warranty not found"}, status=status.HTTP_404_NOT_FOUND)
        warranty.delete()
        return Response({"message": "Warranty deleted successfully"}, status=status.HTTP_200_OK)
    
class AppointmentListCreateAPIView(APIView):
    """
    Handles GET and POST requests for Appointments.
    """
    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppointmentDetailAPIView(APIView):
    """
    Handles GET, PUT, PATCH, and DELETE requests for a single Appointment.
    """
    def get_object(self, pk):
        try:
            return Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            return None

    def get(self, request, pk):
        appointment = self.get_object(pk)
        if not appointment:
            return Response({"error": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        appointment = self.get_object(pk)
        if not appointment:
            return Response({"error": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        appointment = self.get_object(pk)
        if not appointment:
            return Response({"error": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)
        appointment.delete()
        return Response({"message": "Appointment deleted successfully"}, status=status.HTTP_200_OK)
    

class CarClinicListCreateAPIView(APIView):
    """
    Handles GET and POST requests for CarClinic records.
    """
    def get(self, request):
        clinics = CarClinic.objects.all()
        serializer = CarClinicSerializer(clinics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CarClinicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CarClinicDetailAPIView(APIView):
    """
    Handles GET, PUT, PATCH, and DELETE requests for a single CarClinic record.
    """
    def get_object(self, pk):
        try:
            return CarClinic.objects.get(pk=pk)
        except CarClinic.DoesNotExist:
            return None

    def get(self, request, pk):
        clinic = self.get_object(pk)
        if not clinic:
            return Response({"error": "Clinic visit not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarClinicSerializer(clinic)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        clinic = self.get_object(pk)
        if not clinic:
            return Response({"error": "Clinic visit not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarClinicSerializer(clinic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        clinic = self.get_object(pk)
        if not clinic:
            return Response({"error": "Clinic visit not found"}, status=status.HTTP_404_NOT_FOUND)
        clinic.delete()
        return Response({"message": "Clinic visit deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
