from django.db import models

# Create your models here.

class Subject(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.code} {self.name}"

class Quota(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester = models.IntegerField()
    year = models.IntegerField()
    seat = models.IntegerField()
    status = models.BooleanField()

    def __str__(self):
        return f"{self.subject}"

    def is_seat_available(self):
        return self.registants.count() < self.seat

class Registered(models.Model):
    subject = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.subject}"

class Registant(models.Model):
    user = models.CharField(max_length=64)
    quotas = models.ManyToManyField(Quota, blank=True, related_name='registants')

    def __str__(self):
        return f"{self.user}"