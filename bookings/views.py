from django.shortcuts import render
from django.views import generic
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin


class BookingsApproved(LoginRequiredMixin, generic.ListView):
    model = Booking
    queryset = Booking.objects.filter(status=1).order_by('date')
    template_name = 'bookings.html'

class NewBooking(LoginRequiredMixin, generic.edit.CreateView):
    form_class = BookingForm
    model = Booking
    template_name = 'bookings-new.html'    
    success_url = '/bookings'
    

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.customer = self.request.user
        self.object.save()
        return super().form_valid(form)

class BookingsPending(LoginRequiredMixin, generic.ListView):
    model = Booking
    queryset = Booking.objects.filter(status=0).order_by('date')
    template_name = 'bookings-pending.html'


class EditBooking(LoginRequiredMixin, generic.edit.UpdateView):
    form_class = BookingForm
    model = Booking
    template_name = 'bookings-edit.html'
    success_url = '/bookings'
    

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.status = 0
        self.object.save()
        return super().form_valid(form)

class DeleteBooking(LoginRequiredMixin, generic.edit.DeleteView):
    model = Booking
    template_name = 'bookings-delete.html'
    success_url = '/bookings'