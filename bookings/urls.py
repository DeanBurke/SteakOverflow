from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookingsApproved.as_view(), name='booking-approved'),
    path('bookings-new', views.NewBooking.as_view(), name='bookings-new'),
    path('bookings-pending', views.BookingsPending.as_view(), name='bookings-pending'),
    path('bookings-edit/<int:pk>', views.EditBooking.as_view(), name='bookings-edit'),
    path('bookings-delete/<int:pk>', views.DeleteBooking.as_view(), name='bookings-delete'),
]