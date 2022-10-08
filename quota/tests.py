from django.test import TestCase
from quota.models import Subject, Quota, Registant

class QuotaTestCase(TestCase):

    def setUp(self):

        course1 = Subject.objects.create(code="AAA", name="course1")
        quota = Quota.objects.create(
            subject=course1, semester=0, year=2000, seat=2, status=True)

        registant = Registant.objects.create(user="harry")
        quota.registants.add(registant)

    def test_seat_available(self):

        quota = Quota.objects.first()
        self.assertTrue(quota.is_seat_available())

    def test_seat_not_available(self):

        registant1 = Registant.objects.create(
            user="dragon")

        registant2 = Registant.objects.create(
            user="tiger")

        quota = Quota.objects.first()
        quota.registants.add(registant1)
        quota.registants.add(registant2)

        self.assertFalse(quota.is_seat_available())