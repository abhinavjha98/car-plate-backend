from django.db import models
from users.models import CustomUser,Base
# Create your models here.

class CarDetails(Base):
    number_plate = models.CharField(max_length=150, null=True, blank=True)
    car_model = models.CharField(max_length=150, null=True, blank=True)
    car_color = models.CharField(max_length=150, null=True, blank=True)
    car_location = models.CharField(max_length=150, null=True, blank=True)
    car_image = models.ImageField(upload_to='car/', null=True, blank=True)

class PCNCode(Base):
    pcnCode = models.CharField(max_length=150, null=True, blank=True)
    slug = models.SlugField(max_length=200, null=True, unique=True)

class PCNTable(Base):
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE, related_name="pcnUsers")
    carDetails = models.ForeignKey(CarDetails, null=True, on_delete=models.CASCADE, related_name="pcnCars")
    pcnCode = models.ForeignKey(PCNCode, null=True, on_delete=models.CASCADE, related_name="pcnCodes")
    date_of_creation = models.DateTimeField(null=True, blank=True)
    reason = models.CharField(max_length=150, null=True, blank=True)
