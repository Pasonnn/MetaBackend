from django.test import TestCase
from datetime import datetime
from .models import Booking

# Create your tests here.

class BookingModelTest(TestCase):
    def test_booking_creation(self):
        booking = Booking.objects.create(
            first_name='John',
            last_name='Doe',
            guest_count=2,
            reservation_time=datetime.now(),
            comments='Test comment'
        )
        self.assertEqual(booking.first_name, 'John')
        self.assertEqual(booking.last_name, 'Doe')
        self.assertEqual(booking.guest_count, 2)
        self.assertEqual(booking.comments, 'Test comment')

    def test_booking_str_representation(self):
        booking = Booking.objects.create(
            first_name='John',
            last_name='Doe',
            guest_count=2,
            reservation_time=datetime.now(),
            comments='Test comment'
        )
        self.assertEqual(str(booking), 'John Doe : 2')
