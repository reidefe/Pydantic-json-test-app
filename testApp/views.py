from django.shortcuts import render
from rest_framework import viewsets
from .models import Actor, Film
from .serializers import ActorSerializers, FilmSerializers


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializers
    permission_classes = []


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers
    permission_classes = []



