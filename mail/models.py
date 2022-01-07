from django.db import models
import datetime

# Create your models here.
class Mail(models.Model):
	receiver=models.CharField(max_length=100)
	email_address=models.CharField(max_length=100)
	CITY_NAME=(
				('Mumbai','Mumbai'),
	 			('Delhi','Delhi'), 
				('Chennai','Chennai'),
				('banglore','Banglore'),
				('Kolkata','Kolkata'),
			)
	city=models.CharField(max_length=10,choices=CITY_NAME)
	date_time = models.DateTimeField(default=datetime.datetime.now())
