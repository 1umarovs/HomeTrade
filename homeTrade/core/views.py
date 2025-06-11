from django.shortcuts import render
from .serializers import HouseGallerySerializer , HouseSerializer, HouseFeatureSerializer , InquirySerializer
# Create your views here.
from rest_framework import viewsets
from .models import House, houseGallery, houseFeature, Inquiry

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class HouseGalleryViewSet(viewsets.ModelViewSet):
    queryset = houseGallery.objects.all()
    serializer_class = HouseGallerySerializer

class HouseFeatureViewSet(viewsets.ModelViewSet):
    queryset = houseFeature.objects.all()
    serializer_class = HouseFeatureSerializer

class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer


