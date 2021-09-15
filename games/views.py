from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Game
from .serializers import GameSerializer, PopulatedGameSerializer

class GameListView(APIView):
    # permission_classes = (IsAuthenticated,)

    ''' List View for /players INDEX CREATE '''
    def post(self, request):
        serialized_game = GameSerializer(data=request.data)
        if serialized_game.is_valid():
            serialized_game.save()
            return Response(serialized_game.data)
        return Response(serialized_game.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def get(self, request):
        games = Game.objects.all()
        serialized_games = PopulatedGameSerializer(games, many=True)
        return Response(serialized_games.data)

class GameDetailView(RetrieveDestroyAPIView):
    # permission_classes = (IsAuthenticated,)

    ''' Detail View for /players SHOW UPDATE DELETE'''
    queryset = Game.objects.all()
    serializer_class = PopulatedGameSerializer

    def put(self, request, pk):
        try:
            game_to_update = Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serialized_game = GameSerializer(game_to_update, data=request.data)
        if serialized_game.is_valid():
            serialized_game.save()
            return Response(serialized_game.data)
        return Response(serialized_game.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        # Authentication currently commented out!