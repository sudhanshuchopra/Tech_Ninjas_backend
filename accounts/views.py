from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from fcm.models import Device
from fcm.serializers import DeviceSerializer

class DeviceViewSet(viewsets.ModelViewSet):
	queryset = Device.objects.all()
	serializer_class = DeviceSerializer
	
