from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import Patient,Doctor
from django.contrib import auth
from django.http import HttpResponseRedirect

import logging




def index(request):
    return render(request, 'project/index.html')

def patientRegister(request):
    return render(request, 'project/patientRegister.html')

def patientLogin(request):
    return render(request, 'project/patientLogin.html')

def patientinfo(request):
    return render(request, 'project/patientinfo.html')


def register(request):
    errors = Patient.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('project:patientRegister')

    hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = Patient.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], username=request.POST['username'], password=hashed_password, email=request.POST['email'], phonenumber=request.POST['phonenumber'], address=request.POST['address'])
    user.save()
    logging.info(first_name)  # will print a message to the console
    request.session['id'] = user.id
    messages.success(request, "You Successfully register..")
    return redirect('project:patientLogin')

def login(request):  
    if (Patient.objects.filter(username=request.POST['username']).exists()):
        user = Patient.objects.filter(username=request.POST['username'])[0]
        if (request.POST['password'], user.password):
            request.session['id'] = user.id
            return redirect('project:patientinfo')
    return redirect('project:patientLogin')

def doctorRegister(request):
    return render(request, 'project/doctorRegister.html')

def doctorLogin(request):
    return render(request, 'project/doctorLogin.html')

def doctor_register(request):
    errors = Doctor.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('project:doctorRegister')
    hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = Doctor.objects.create(temp = temp,doctor_name=request.POST['doctor_name'], location=request.POST['location'], password=hashed_password, address=request.POST['address'], phonenumber=request.POST['phonenumber'], shedule=request.POST['shedule'], fees=request.POST['fees'])
    user.save()
    request.session['id'] = user.id
    messages.success(request, "You Successfully register..")
    return redirect('project:doctorLogin')

def doctor_login(request):
    if (Doctor.objects.filter(doctor_name=request.POST['doctor_name']).exists()):
        user = Doctor.objects.filter(doctor_name=request.POST['doctor_name'])[0]
        if (request.POST['password'], user.password):
            request.session['id'] = user.id
            return redirect('project:doctorinfo')
    return redirect('project:doctorLogin')

def doctorinfo(request):
    return render(request, 'project/doctorinfo.html')