from django.test import TestCase
from .models import Subject, Quota, Registant, Registered


class QuotaModelTestCase(TestCase):

    def setUp(self):
        subject1 = Subject.objects.create(code='AAA', name='Subject A')
        Quota.objects.create(subject=subject1, semester=1, year=1, seat=1, status=True)
        Registered.objects.create(subject=subject1)
        Registant.objects.create(user='harry')

    def test_subject_model(self):
        subject = Subject.objects.get(code='AAA')
        self.assertEqual(subject.name, 'Subject A')

        # Test class Subject in models.

    def test_quota_model(self):
        subject1 = Subject.objects.first()
        quota = Quota.objects.get(subject=subject1)
        self.assertEqual(str(subject1), str(quota))

        # Test class Quota in models.

    def test_registered_model(self):
        subject1 = Subject.objects.first()
        registered = Registered.objects.get(subject=subject1)
        self.assertEqual(str(subject1), str(registered))

        # Test class Registered in models.

    def test_registant_model(self):
        registant = Registant.objects.get(user='harry')
        self.assertEqual(str(registant), 'harry')

        # Test class Registant in models.