from django.http import HttpResponse
from django.shortcuts import render
from . models import Job


def magic(request):
    obj = Job.objects.all()
    return render(request, "index.html", {'result': obj})
