from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(ModelAdmin):
    list_display = ('customer', 'reference', 'date', 'time', 'group_size', 'status')
    search_fields = ('customer', 'reference''date', 'group_size', 'status')
    list_filter = ('date', 'status')
    actions = ['pending_booking', 'approve_booking', 'deny_booking']

    def pending_booking(self, request, queryset):
        queryset.update(status=0)

    def approve_booking(self, request, queryset):
        queryset.update(status=1)

    def deny_booking(self, request, queryset):
        queryset.update(status=2)