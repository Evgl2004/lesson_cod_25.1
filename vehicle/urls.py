from vehicle.apps import VehicleConfig
from rest_framework.routers import DefaultRouter
from vehicle.views import CarViewSet
from django.urls import path

from vehicle.views import (MotoCreateAPIView, MotoListAPIView, MotoRetrieveAPIView, MotoUpdateAPIView,
                           MotoDestroyAPIView, MileageCreateAPIView, MotoMileageListAPIView, MileageListAPIView)

app_name = VehicleConfig.name

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')

urlpatterns = [
    path('moto/create/', MotoCreateAPIView.as_view(), name='moto_create'),
    path('moto/list/', MotoListAPIView.as_view(), name='moto_list'),
    path('moto/view/<int:pk>/', MotoRetrieveAPIView.as_view(), name='moto_view'),
    path('moto/edit/<int:pk>/', MotoUpdateAPIView.as_view(), name='moto_edit'),
    path('moto/delete/<int:pk>/', MotoDestroyAPIView.as_view(), name='moto_delete'),
    path('mileage/create/', MileageCreateAPIView.as_view(), name='mileage_create'),
    path('moto_mileage/list/', MotoMileageListAPIView.as_view(), name='moto_mileage_list'),
    path('mileage/list/', MileageListAPIView.as_view(), name='mileage_list')
] + router.urls
