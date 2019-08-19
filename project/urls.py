from django.conf.urls import url,include
from django.urls import path


from . import views

app_name = 'project'

urlpatterns = [
    path('', views.index, name="index"),
    url(r'^patientRegister/$', views.patientRegister, name="patientRegister"),
    url(r'^register$', views.register, name="register"),
    url(r'^doctorRegister/$', views.doctorRegister, name="doctorRegister"),
    url(r'^doctor_register$', views.doctor_register, name="doctor_register"),
    url(r'^patientLogin/$', views.patientLogin, name="patientLogin"),
    url(r'^login$', views.login, name="login"),
    url(r'^doctor_login$', views.doctor_login, name="doctor_login"),
    url(r'^doctorLogin/$', views.doctorLogin, name="doctorLogin"),
    url(r'^patientinfo$', views.patientinfo, name="patientinfo"),
    url(r'^doctorinfo$', views.doctorinfo, name="doctorinfo"),
]
