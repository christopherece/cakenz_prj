from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def index(request):
    return render(request, 'pages/index.html')