from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from musics.models import CD
from musics.serializers import CDSerializer


# Create your views here.
class CDViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = CD.objects.all()
    serializer_class = CDSerializer