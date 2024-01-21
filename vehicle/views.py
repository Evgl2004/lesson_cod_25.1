from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from vehicle.serializers import (CarSerializer, MotoSerializer, MileageSerializer, MotoMileageSerializer,
                                 MotoCreateSerializer)
from vehicle.models import Car, Moto, Mileage


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoCreateSerializer


class MotoListAPIView(generics.ListAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoDestroyAPIView(generics.DestroyAPIView):
    queryset = Moto.objects.all()


class MileageCreateAPIView(generics.CreateAPIView):
    serializer_class = MileageSerializer


class MotoMileageListAPIView(generics.ListAPIView):
    serializer_class = MotoMileageSerializer
    queryset = Mileage.objects.filter(moto__isnull=False)


class MileageListAPIView(generics.ListAPIView):
    serializer_class = MileageSerializer
    queryset = Mileage.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('car', 'moto')
    ordering_field = ('year', )

