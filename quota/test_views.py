from django.test import TestCase, Client
from django.urls import reverse
from django.db.models import Max
from .models import Subject, Quota, Registant


class QuotaViewTestCase(TestCase):

    def setUp(self):
        
        course1 = Subject.objects.create(code="AAA", name="course1")
        quota = Quota.objects.create(
            subject=course1, semester=0, year=2000, seat=2, status=True)

        registant = Registant.objects.create(user="harry")
        quota.registants.add(registant)

    def test_index_view_status_code(self):
        c = Client()
        response = c.get(reverse('quotas:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_context(self):
        c = Client()
        response = c.get(reverse('quotas:index'))
        self.assertEqual(
            response.context['quota'].count(), 1)

    def test_valid_quota_page(self):
        c = Client()
        q = Quota.objects.first()
        response = c.get(reverse('quotas:quota', args=(q.id,)))
        self.assertEqual(response.status_code, 200)

    def test_invalid_quota_page(self):
        max_id = Quota.objects.all().aggregate(Max("id"))['id__max']

        c = Client()
        response = c.get(reverse('quotas:quota', args=(max_id+1,)))
        self.assertEqual(response.status_code, 404)