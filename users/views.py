from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from quota import models
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'users/index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'users/login.html', {
                'message': 'Invalid credentials.'
            })

    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {
        'message': 'Logged out.'
    })


def registered(request):
    subjects = models.Registered.objects.all()
    if request.method == "POST":
        registed = request.POST['registed']
        subject = models.Registered(subject=registed)
        subject.save()
        cal_seat(subject, -1)
    return render(request, 'users/registered.html', {
        'subjects': subjects,
    })


def delete(request):
    if request.method == "POST":
        subject = request.POST.get('delete')
        cal_seat(subject, 1)
        models.Registered.objects.filter(subject=subject).delete()
        subjects = models.Registered.objects.all()
    return render(request, 'users/registered.html', {
        'message': 'Deleted.',
        'subjects': subjects,
    })

def cal_seat(obj, count):
    quota = models.Quota.objects.all()
    for q in quota:
        if obj == q:
            q.seat += count
            q.save()