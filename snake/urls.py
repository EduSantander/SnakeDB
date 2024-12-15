from django.urls import path
from snake import views

urlpatterns = [
    path('jugadores/', views.jugador_list.as_view() ),
    path('jugadores/<int:pk>/', views.jugador_detail.as_view() ),
]