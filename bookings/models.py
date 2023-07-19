from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

BOOKING_STATUS = ((0, "Pending"), (1, "Approved"), (2, "Denied"))

class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    reference = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField(default=(19, 30))
    group_size = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=BOOKING_STATUS, default=0)

    class Meta:
        ordering = ['-date']
