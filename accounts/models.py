from django.db import models

# Create your models here.
from fcm.models import AbstractDevice
class MyDevice(AbstractDevice):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)

