from rest_framework import serializers
from .models import House, houseGallery, houseFeature, Inquiry

class HouseGallerySerializer(serializers.ModelSerializer):
    house = serializers.PrimaryKeyRelatedField(queryset=House.objects.all())

    class Meta:
        model = houseGallery
        fields = ['id', 'house', 'image']


class HouseFeatureSerializer(serializers.ModelSerializer):
    house = serializers.PrimaryKeyRelatedField(queryset=House.objects.all())

    class Meta:
        model = houseFeature
        fields = '__all__'


class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        exclude = ['house']


class HouseSerializer(serializers.ModelSerializer):
    gallery = HouseGallerySerializer(many=True, read_only=True)
    features = HouseFeatureSerializer(many=True, read_only=True)
    inquiries = InquirySerializer(many=True, read_only=True)

    class Meta:
        model = House
        fields = '__all__'
