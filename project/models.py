from __future__ import unicode_literals
from django.db import models
from django.http import HttpResponse

class PatientManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['first_name'].isalpha()) == False:
            if len(postData['first_name']) < 2:
                errors['first_name'] = "First name can not be shorter than 2 characters"

        if (postData['last_name'].isalpha()) == False:
            if len(postData['last_name']) < 2:
                errors['last_name'] = "Last name can not be shorter than 2 characters"

        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"
        
        if len(postData['username']) == 0:
            errors['username'] = "You must enter an username"
        
        if len(postData['phonenumber']) == 0:
            errors['phonenumber'] = "You need to enter your phone number"

        if len(postData['address']) == 0:
            errors['address'] = "You need to enter your address"

        if len(postData['password']) < 8:
            errors['password'] = "Password is too short!"

        return errors

class DoctorManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['doctor_name'].isalpha()) == False:
            if len(postData['doctor_name']) < 2:
                errors['doctor_name'] = "Doctor name can not be shorter than 2 characters"

        if len(postData['location']) == 0:
            errors['location'] = "You must enter an location"
        
        if len(postData['address']) == 0:
            errors['address'] = "You must enter an address"
        
        if len(postData['phonenumber']) == 0:
            errors['phonenumber'] = "You need to enter your phone number"

        if len(postData['shedule']) == 0:
            errors['shedule'] = "You need to enter your shedule"
        
        if len(postData['fees']) == 0:
            errors['fees'] = "You need to enter your fees"

        if len(postData['password']) < 8:
            errors['password'] = "Password is too short!"

        return errors

class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = PatientManager()
    def __str__(self):
        return self.username


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=255)
    diabetes_specialist = models.BooleanField(default=True)
    location = models.CharField(max_length=255)
    address = models.TextField(max_length=255)
    phonenumber = models.CharField(max_length=255)
    shedule = models.CharField(max_length=255)
    fees = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = DoctorManager()
    def __str__(self):
        return self.doctor_name

