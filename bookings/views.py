from django.shortcuts import render
from django.views import generic
from .models import Booking


class BookingsApproved(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter(status=1).order_by('date')
    template_name = 'bookings.html'