from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def home(request):
     if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        mobile_no = request.POST.get("mobile_number")
        date = request.POST.get("created_at")
        flight_name = request.POST.get("flight_name")
        flight_no = request.POST.get("flight_no")
        flight_date = request.POST.get("created_at")
        flight_cancellation = request.POST.get("flight")
        flight_hour = request.POST.get("flight_hour")
        flight_days = request.POST.get("flight_days")
    
        select = request.POST.get("select")
        flight = Flight.objects.create(first_name = first_name, last_name = last_name, mobile_no = mobile_no, date = date, flight_name = flight_name, flight_no = flight_no, flight_date = flight_date, flight_cancellation = flight_cancellation, flight_hour = flight_hour, flight_days = flight_days, select = select)
        flight.save()
        return redirect('/')
    
     return render(request,'home.html')
    
