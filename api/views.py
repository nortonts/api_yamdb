from rest_framework import viewsets, generics, filters
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ViewSetMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import *
from .permissions import AdminOrReadOnly, IsAdminUser
from .serializers import *
from rest_framework.generics import DestroyAPIView
from rest_framework.mixins import DestroyModelMixin
from django.http import response
from rest_framework import status

class TitleView(viewsets.ModelViewSet):
    permission_classes = (AdminOrReadOnly, IsAdminUser)
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'year', 'genre', 'category',)

    def perform_create(self, serializer):
        serializer.save()


class GenreView(viewsets.ModelViewSet):
    permission_classes = (AdminOrReadOnly, IsAdminUser)
    queryset = Genre.objects.all()
    lookup_field = 'slug'
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def retrieve(self, request, *args, **kwargs):
       return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)  


class CategoryView(viewsets.ModelViewSet):
    permission_classes = (AdminOrReadOnly, IsAdminUser)
    queryset = Category.objects.all()
    lookup_field = 'slug'
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def retrieve(self, request, *args, **kwargs):
       return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED) 