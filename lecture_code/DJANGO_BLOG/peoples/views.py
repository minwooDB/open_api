from django.shortcuts import render, redirect
from .models import People
from  faker import Faker

def index(request):
    peoples = People.objects.all()
    return render(request,"peoples/index.html",{'peoples':peoples})

def create(request):
    fake= Faker('ko_KR')
    people = People()
    people.name = fake.name()
    people.job = fake.job()
    people.address = fake.address()
    people.save()

    return redirect('/peoples')

def delete(request, pk):
    people= People.objects.get(pk=pk)
    people.delete()
    return redirect('/peoples')


