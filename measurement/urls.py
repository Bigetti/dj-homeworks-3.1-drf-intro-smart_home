from django.urls import path
from .views import CreateSensorView, SensorDetailView, AddMeasurementView, GetSensorListView

urlpatterns = [
    path('create-sensor/', CreateSensorView.as_view(), name='create_sensor'),
   # path('update-sensor/<int:pk>/', UpdateSensorView.as_view(), name='update_sensor'),
    path('add-measurement/', AddMeasurementView.as_view(), name='add_measurement'),
    path('get-sensor-list/', GetSensorListView.as_view(), name='get_sensor_list'),
    #path('get-sensor-info/<int:id>/', GetSensorInfoView.as_view(), name='get_sensor_info'),
    path('sensor/<int:id>/', SensorDetailView.as_view(), name='sensor_detail'),
    # Другие маршруты...
]

