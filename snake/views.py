from rest_framework import generics
from snake.models import Jugador
from snake.serializers import JugadorSerializer

class jugador_list(generics.ListCreateAPIView):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer

class jugador_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer
