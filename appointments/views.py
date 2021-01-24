from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Appointment


# Create your views here.
def index(request):
    all_appointments = Appointment.objects.all()
    template = loader.get_template('appointments/index.html')
    context = {
        'all_appointments': all_appointments
    }
    return HttpResponse(template.render(context, request))


def create(request):
    a = Appointment(name=request.POST['name'], phone_number=request.POST['number'], date=request.POST['date'])
    a.save()
    all_appointments = Appointment.objects.all()
    template = loader.get_template('appointments/index.html')
    context = {
        'all_appointments': all_appointments
    }
    return HttpResponse(template.render(context, request))

