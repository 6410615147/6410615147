from django.contrib import admin
from .models import Registered, Quota, Subject
# Register your models here.


class QuotaAdmin(admin.ModelAdmin):
    list_display = ['subject', 'semester', 'year', 'seat', 'status']

admin.site.register(Quota, QuotaAdmin)
admin.site.register(Subject)
admin.site.register(Registered)