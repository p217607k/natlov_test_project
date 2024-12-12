from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cars")
    model = models.CharField(max_length=255)
    license_plate = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(
        max_length=2,
        choices=[('2W', '2-Wheel'), ('4W', '4-Wheel')],
        default='4W'
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.model} - {self.license_plate}"
class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} (${self.price})"
class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="orders")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="orders")
    order_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order for {self.car.model} - {self.service.name}"
class WorkLog(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="work_log")
    performed_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Work Log for {self.order}"
class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="payment")
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    is_successful = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment for {self.order.car.model} - ${self.amount_paid}"
class Review(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="review")
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Review for {self.order.car.model}"
class License(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name="license")
    license_type = models.CharField(max_length=100)
    expiry_date = models.DateField()

    def __str__(self):
        return f"License for {self.car.model} ({self.license_type})"
class Warranty(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="warranties")
    warranty_period = models.PositiveIntegerField()  # in months
    coverage = models.TextField()

    def __str__(self):
        return f"Warranty for {self.car.model} - {self.warranty_period} months"
class Appointment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="appointments")
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Appointment for {self.car.model} - {self.service.name}"
class CarClinic(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="clinic_visits")
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    visit_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Clinic Visit for {self.car.model} - {self.service.name}"
