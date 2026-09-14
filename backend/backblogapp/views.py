from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import postserializers
from .models import post


class PostModelViewSet(ModelViewSet):
    serializer_class = postserializers
    queryset = post.objects.all()
    lookup_field = 'slug'

    @action(detail=False, methods=['Get']) 
    def recent(self, request):
        posts = post.objects.all()[:6]
        serializer = postserializers(posts, many=True)
        return Response(serializer.data)
