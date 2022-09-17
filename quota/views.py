from django.shortcuts import render

from .models import Quota
# Create your views here.

def index(request):
    quota = Quota.objects.all()
    return render(request, 'quota/index.html', {
        'quota': quota,
    })

def quota(request, quota_id):
    quota = Quota.objects.get(id=quota_id)
    return render(request, 'quota/quota.html', {
        'quota': quota
    })
