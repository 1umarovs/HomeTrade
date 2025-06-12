from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HouseViewSet,
    HouseGalleryViewSet,
    HouseFeatureViewSet,
    InquiryViewSet
)

router = DefaultRouter()
router.register(r'houses', HouseViewSet)
router.register(r'galleries', HouseGalleryViewSet)
router.register(r'features', HouseFeatureViewSet)
router.register(r'inquiries', InquiryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
