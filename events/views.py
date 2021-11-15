from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import HackathonSerializer, WorkshopSerializer
from .models import Hackathon, Workshop


class HackathonViewSet(viewsets.ModelViewSet):
    queryset = Hackathon.objects.all().order_by('start')
    serializer_class = HackathonSerializer

class WorkshopViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all().order_by('hackathon')
    serializer_class = WorkshopSerializer