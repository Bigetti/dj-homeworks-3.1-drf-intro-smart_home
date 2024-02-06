from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorDetailSerializer


# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

# Создать датчик
# POST
class CreateSensorView(generics.CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer



# Обновить датчик и получить информацию о конкретном датчике
# PUT (обновление) и GET (получение)
class SensorDetailView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    lookup_field = 'id'


# # Изменить датчик
# # PUT
# class UpdateSensorView(generics.UpdateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer


# Добавить измерение
# POST
class AddMeasurementView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


# Получить список датчиков
# GET
class GetSensorListView(generics.ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# # Получить информацию по конкретному датчику
# # GET
# class GetSensorInfoView(generics.RetrieveAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer
#     lookup_field = 'id'
