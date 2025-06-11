# core/serializers.py
from rest_framework import serializers
from .models import House, houseGallery, houseFeature, Inquiry

class HouseGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = houseGallery
        fields = ['id', 'image']

class HouseFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = houseFeature
        fields = '__all__' 

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):
    gallery = HouseGallerySerializer(many=True)
    features = HouseFeatureSerializer(many=True)
    inquiries = InquirySerializer(many=True)

    class Meta:
        model = House
        fields = '__all__'
