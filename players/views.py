
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Player
from .serializers import PlayerSerializer

class PlayerListView(ListCreateAPIView):
    ''' List View for /players INDEX CREATE '''
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerDetailView(RetrieveUpdateDestroyAPIView):
    ''' Detail View for /players SHOW UPDATE '''
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

# class PlayerListView(APIView):
#     ''' List View for /players GET POST '''

#     def get(self, _request):
#         ''' Index '''
#         players = Player.objects.all()
#         serialized = PlayerSerializer(players, many=True)
#         return Response(serialized.data, status=status.HTTP_200_OK)

# class PlayerDetailView(APIView):
#     ''' Detail View for /players/id '''

#     def get(self, _request, player_pk):
#         player = Player.objects.get(pk=player_pk)
#         serialized = PlayerSerializer(player)
#         return Response(serialized.data, status=status.HTTP_200_OK)
