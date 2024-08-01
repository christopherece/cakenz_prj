from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def service(request):
    return render(request, 'pages/service.html')


def team(request):
    return render(request, 'pages/team.html')