from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255, db_column='Name')
    no_of_guests = models.IntegerField(db_column='No_of_guests')
    booking_date = models.DateTimeField(db_column='BookingDate')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Booking'


class Menu(models.Model):
    title = models.CharField(max_length=255, db_column='Title')
    price = models.DecimalField(max_digits=10, decimal_places=2, db_column='Price')
    inventory = models.IntegerField(db_column='Inventory')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Menu'