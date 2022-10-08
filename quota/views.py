from django.shortcuts import render, get_object_or_404

from .models import Quota
# Create your views here.

def index(request):
    quota = Quota.objects.all()
    return render(request, 'quota/index.html', {
        'quota': quota,
    })

def quota(request, quota_id):
    quota = get_object_or_404(Quota, pk=quota_id)
    return render(request, 'quota/quota.html', {
        'quota': quota
    })
