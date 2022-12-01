from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from musics.models import CD
from musics.serializers import CDSerializer
from musics.permissions import IsPublisherOrReadOnly

# Create your views here.
class CDViewSet(viewsets.ModelViewSet):
    permission_classes = [IsPublisherOrReadOnly|permissions.IsAdminUser]
    queryset = CD.objects.all()
    serializer_class = CDSerializer


#CDByArtist,CDByPublishedBy,CDByName
class CDByArtist(generics.ListAPIView):
    permission_classes = [IsPublisherOrReadOnly|permissions.IsAdminUser]
    model = CD
    serializer_class = CDSerializer

    def get_queryset(self):
        artist = self.request.query_params.get('artist')
        cd_by_artist = CD.objects.filter(artist=artist)
        return cd_by_artist

class CDByName(generics.ListAPIView):
    permission_classes = [IsPublisherOrReadOnly|permissions.IsAdminUser]
    model = CD
    serializer_class = CDSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        cd_by_name = CD.objects.filter(name=name)
        return cd_by_name

class CDByPublishedBy(generics.ListAPIView):
    permission_classes = [IsPublisherOrReadOnly|permissions.IsAdminUser]
    model = CD
    serializer_class = CDSerializer

    def get_queryset(self):
        publishedby = self.request.query_params.get('publishedby')
        cd_by_published = CD.objects.filter(published_by=publishedby)
        return cd_by_published
