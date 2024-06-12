from django.contrib import admin
from django.urls import path

from fire.views import HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity
from fire import views
from fire.views import LocationList, IncidentList, FireStationList, FireFighterList, FireTruckList, WeatherConditionList, LocationCreateView, IncidentCreateView, FireStationCreateView, FireFighterCreateView, FireTruckCreateView, WeatherConditionCreateView, LocationUpdateView, IncidentUpdateView, FireStationUpdateView, FireFighterUpdateView, FireTruckUpdateView, WeatherConditionUpdateView, LocationDeleteView, IncidentDeleteView, FireStationDeleteView, FireFighterDeleteView, FireTruckDeleteView, WeatherConditionDeleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('chart/', PieCountbySeverity, name='chart'),
    path('lineChart/', LineCountbyMonth, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multiBarChart/', multipleBarbySeverity, name='chart'),
    path('stations', views.map_station, name='map-station'),
    path('incidents', views.map_incident, name='fire-incident'),
    path('location_list', LocationList.as_view(), name='location'),
    path('incident_list', IncidentList.as_view(), name='incident'),
    path('firestation_list', FireStationList.as_view(), name='fire-station'),
    path('firefighter_list', FireFighterList.as_view(), name='fire-fighter'),
    path('firetruck_list', FireTruckList.as_view(), name='fire-truck'),
    path('weathercondition_list', WeatherConditionList.as_view(), name='weather-condition'),
    path('location_list/add', LocationCreateView.as_view(), name='loc-add'),
    path('incident_list/add', IncidentCreateView.as_view(), name='incident-add'),
    path('firestation_list/add', FireStationCreateView.as_view(), name='station-add'),
    path('firefighter_list/add', FireFighterCreateView.as_view(), name='fighter-add'),
    path('firetruck_list/add', FireTruckCreateView.as_view(), name='truck-add'),
    path('weathercondition_list/add', WeatherConditionCreateView.as_view(), name='weather-add'),
    path('location_list/<pk>', LocationUpdateView.as_view(), name='loc-edit'),
    path('incident_list/<pk>', IncidentUpdateView.as_view(), name='incident-edit'),
    path('firestation_list/<pk>', FireStationUpdateView.as_view(), name='station-edit'),
    path('firefighter_list/<pk>', FireFighterUpdateView.as_view(), name='fighter-edit'),
    path('firetruck_list/<pk>', FireTruckUpdateView.as_view(), name='truck-edit'),
    path('weathercondition_list/<pk>', WeatherConditionUpdateView.as_view(), name='weather-edit'),
    path('location_list/<pk>/delete', LocationDeleteView.as_view(), name='loc-delete'),
    path('incident_list/<pk>/delete', IncidentDeleteView.as_view(), name='incident-delete'),
    path('firestation_list/<pk>/delete', FireStationDeleteView.as_view(), name='station-delete'),
    path('firefighter_list/<pk>/delete', FireFighterDeleteView.as_view(), name='fighter-delete'),
    path('firetruck_list/<pk>/delete', FireTruckDeleteView.as_view(), name='truck-delete'),
    path('weathercondition_list/<pk>/delete', WeatherConditionDeleteView.as_view(), name='weather-delete'),
    
]
