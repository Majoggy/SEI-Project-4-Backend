from players.serializers import PlayerSerializer
from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = '__all__'

class PopulatedGameSerializer(GameSerializer):
    first_place = PlayerSerializer()
    second_place = PlayerSerializer()
    third_place = PlayerSerializer()
    fourth_place = PlayerSerializer()
    fifth_place = PlayerSerializer()
    sixth_place = PlayerSerializer()
    seventh_place = PlayerSerializer()
    eighth_place = PlayerSerializer()
    ninth_place = PlayerSerializer()