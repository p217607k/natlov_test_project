from django.test import TestCase
from django.contrib.auth.models import User
from .models import Car, Bill

class CarModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.car = Car.objects.create(
            user=self.user,
            model="Toyota Camry",
            license_plate="XYZ123",
            is_completed=False
        )

    def test_car_creation(self):
        self.assertEqual(Car.objects.count(), 1)
        self.assertEqual(self.car.model, "Toyota Camry")
        self.assertFalse(self.car.is_completed)

    def test_car_str_representation(self):
        self.assertEqual(str(self.car), self.car.model)


class BillModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.car = Car.objects.create(
            user=self.user,
            model="Toyota Camry",
            license_plate="XYZ123",
            is_completed=False
        )
        self.bill = Bill.objects.create(
            car=self.car,
            amount=100.50,
            paid=False
        )

    def test_bill_creation(self):
        self.assertEqual(Bill.objects.count(), 1)
        self.assertEqual(self.bill.amount, 100.50)
        self.assertFalse(self.bill.paid)

    def test_bill_str_representation(self):
        self.assertEqual(str(self.bill), f"Bill for {self.bill.car.model}")
