from django.db import models

class Booking(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    booking_date = models.DateField()
    created_at = models.DateField()
    modified_at = models.DateField()
    is_canceled = models.BooleanField(default=False)
    canceled_at = models.DateField()
    total_price = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    stay_from = models.DateField()
    stay_to = models.DateField()
