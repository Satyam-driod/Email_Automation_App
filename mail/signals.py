from django.db.models.signals import post_save
from django.dispatch import receiver
from .weather import getWeatherDetails

from .models import Mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

@receiver(post_save,sender=Mail)
def sendMail(sender,instance,created,**kwargs):
	
	if created:
		temp=getWeatherDetails(instance.city)
		degree_sign = u'\N{DEGREE SIGN}'
		if(temp<17):
		    emozi='❄'
		elif(temp>17 and temp<23):
			emozi='🌞'
		else:
			emozi='🔥'

		email=EmailMessage(
			f'Hi {instance.receiver},intrested in our services',
			f'the temp of your city is {temp}{degree_sign}C{emozi}',
			settings.EMAIL_HOST_USER,
			[instance.email_address],
		)
		email.fail_silently=False
		email.send()


		