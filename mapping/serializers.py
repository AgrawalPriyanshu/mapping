from rest_framework import serializers
from .models import Registration,Game,Athlete

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model=Registration
        fields='__all__'

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model=Game
        fields='__all__'

class AthleteSerializer(serializers.ModelSerializer):

    class Meta:
        model=Athlete
        fields='__all__'
