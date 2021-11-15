from rest_framework import serializers

from .models import Hackathon, Workshop

class WorkshopSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Workshop
        fields = ('id', 'title', 'extract', 'start', 'end', 'max_participants', 'participants', 'hackathon', 'organizer')
class HackathonSerializer(serializers.ModelSerializer):
    workshops = WorkshopSerializer(many=True, read_only=True)
    class Meta:
        model = Hackathon
        fields = ('id', 'title', 'extract', 'start', 'end', 'max_participants', 'participants', 'workshops')
