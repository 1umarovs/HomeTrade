from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', HouseViewSet.as_view({'get': 'list', 'post': 'create'}), name='house-list'),
    path('gallery/', HouseGalleryViewSet.as_view({'get': 'list', 'post': 'create'}), name='house-gallery-list'),
    path('features/', HouseFeatureViewSet.as_view({'get': 'list', 'post': 'create'}), name='house-feature-list'),
    path('inquiries/', InquiryViewSet.as_view({'get': 'list', 'post': 'create'}), name='inquiry-list'),
]