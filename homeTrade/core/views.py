from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny , IsAuthenticated

from .models import House, houseGallery, houseFeature, Inquiry
from .serializers import (
    HouseSerializer,
    HouseGallerySerializer,
    HouseFeatureSerializer,
    InquirySerializer,
)

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

    def get_permissions(self):
        if self.action in ['add_feature', 'add_gallery']:
            return [IsAdminUser()]
        elif self.action == 'add_inquiry':
            return [AllowAny()]
        return super().get_permissions()
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return super().get_permissions()

    @action(detail=True, methods=['post'], url_path='add-feature')
    def add_feature(self, request, pk=None):
        house = self.get_object()
        serializer = HouseFeatureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(house=house)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], url_path='add-gallery')
    def add_gallery(self, request, pk=None):
        house = self.get_object()
        serializer = HouseGallerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(house=house)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], url_path='add-inquiry')
    def add_inquiry(self, request, pk=None):
        house = self.get_object()
        serializer = InquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(house=house)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HouseGalleryViewSet(viewsets.ModelViewSet):
    queryset = houseGallery.objects.all()
    serializer_class = HouseGallerySerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return super().get_permissions()

class HouseFeatureViewSet(viewsets.ModelViewSet):
    queryset = houseFeature.objects.all()
    serializer_class = HouseFeatureSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return super().get_permissions()


class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return super().get_permissions()



