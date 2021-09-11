from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Player
from .serializers import PlayerSerializer

class PlayerListView(ListCreateAPIView):
    ''' List View for /players INDEX CREATE '''
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    # permission_classes = (IsAuthenticated,)

class PlayerDetailView(RetrieveUpdateDestroyAPIView):
    ''' Detail View for /players SHOW UPDATE '''
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    # permission_classes = (IsAuthenticated,)

# Authentication currently commented out!