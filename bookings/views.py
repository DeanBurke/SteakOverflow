from django.shortcuts import render
from django.views import generic
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin


class BookingsApproved(LoginRequiredMixin, generic.ListView):
    model = Booking
    queryset = Booking.objects.filter(status=1).order_by('date')
    template_name = 'bookings.html'