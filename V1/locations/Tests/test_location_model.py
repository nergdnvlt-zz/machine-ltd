from django.test import TestCase
from V1.locations.models import Location
from V1.devices.models import Device
from V1.users.models import User

# python manage.py test V1/locations/tests

class LocationModelTestCase(TestCase):

    def test_device_saves_to_db(self):
        user = User.objects.create(username='Thrasher',
                                   phone_number='7196639883',)
        device = Device.objects.create(user=user,
                                       sms_number='7192710056',
                                       pin_lat=39.996665,
                                       pin_long=-105.234931)

        input_location = Location.objects.create(device=device, lat=39.996665, long=-105.234931)

        saved_location = Location.objects.first()
        count = Location.objects.count()

        self.assertEqual(saved_location.lat, 39.996665)
        self.assertEqual(saved_location.long, -105.234931)
        self.assertEqual(saved_location.device.id, device.id)
        self.assertEqual(count, 1)

    def test_device_calculates_distance(self):
        user = User.objects.create(username='Thrasher',
                                   phone_number='7196639883',)
        device = Device.objects.create(user=user,
                                       sms_number='7192710056',
                                       pin_lat=39.996665,
                                       pin_long=-105.234931)

        input_location = Location.objects.create(device=device, lat=39.996665, long=-105.234931)

        saved_location = Location.objects.first()

        self.assertEqual(saved_location.lat, 39.996665)
        self.assertEqual(saved_location.long, -105.234931)
        self.assertEqual(saved_location.distance, 0)
