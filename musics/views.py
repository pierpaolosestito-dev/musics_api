from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from musics.models import CD
from musics.serializers import CDSerializer
from musics.permissions import IsPublisherOrReadOnly


class CDViewSet(viewsets.ModelViewSet):
    permission_classes = [IsPublisherOrReadOnly | permissions.IsAdminUser]
    queryset = CD.objects.all()
    serializer_class = CDSerializer
