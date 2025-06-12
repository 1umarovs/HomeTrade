from rest_framework import serializers
from .models import House, houseGallery, houseFeature, Inquiry
from django.utils.text import slugify


class HouseGallerySerializer(serializers.ModelSerializer):
    house = serializers.PrimaryKeyRelatedField(queryset=House.objects.all())  # ✅ Dropdown-style

    class Meta:
        model = houseGallery
        fields = ['id', 'house', 'image']  # ✅ exclude o‘rniga fields yozildi


class HouseFeatureSerializer(serializers.ModelSerializer):
    house = serializers.PrimaryKeyRelatedField(queryset=House.objects.all())  # ✅ Dropdown-style

    class Meta:
        model = houseFeature
        fields = '__all__'  # ✅ exclude emas


class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        exclude = ['house']  # bu joy to‘g‘ri, chunki house ni view orqali biriktirasan


class HouseSerializer(serializers.ModelSerializer):
    gallery = HouseGallerySerializer(many=True, read_only=True)
    features = HouseFeatureSerializer(many=True, read_only=True)
    inquiries = InquirySerializer(many=True, read_only=True)

    class Meta:
        model = House
        fields = '__all__'
        extra_kwargs = {
            'slug': {'required': False},
        }

    def create(self, validated_data):
        if 'slug' not in validated_data or not validated_data['slug']:
            validated_data['slug'] = slugify(validated_data.get('title', ''))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'slug' not in validated_data or not validated_data['slug']:
            validated_data['slug'] = slugify(validated_data.get('title', instance.title))
        return super().update(instance, validated_data)
