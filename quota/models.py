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
        return f"{self.id}. {self.subject} ==> Seat remaining: {self.seat}"


class Registant(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    quotas = models.ManyToManyField(Quota, blank = True, related_name='registant')

    def __str__(self):
        return f"{self.first} {self.last}"