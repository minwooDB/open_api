from django.shortcuts import render, redirect
from .models import Student

def index(request):
    student = Student.objects.order_by('-pk')
    return render(request,'students/index.html',{'student':student})