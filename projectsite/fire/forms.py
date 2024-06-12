from django import forms
from .models import Locations, Incident, FireStation, Firefighters, FireTruck, WeatherConditions
from django.forms import ModelForm

class CityFilterForm(forms.Form):
    # Query the unique cities from the Locations table
    city_choices = Locations.objects.order_by('city').values_list('city', 'city').distinct()
    city_choices = [('all', 'All Cities')] + list(city_choices)

    city = forms.ChoiceField(choices=city_choices, label='Filter by City')

class LocationForm(ModelForm):
    class Meta:
        model = Locations
        fields = "__all__"

class IncidentForm(ModelForm):
    class Meta:
        model = Incident
        fields = "__all__"

class FireStationForm(ModelForm):
    class Meta:
        model = FireStation
        fields = "__all__"

class FireFighterForm(ModelForm):
    class Meta:
        model = Firefighters
        fields = "__all__"

class FireTruckForm(ModelForm):
    class Meta:
        model = FireTruck
        fields = "__all__"

class WeatherConditionForm(ModelForm):
    class Meta:
        model = WeatherConditions
        fields = "__all__"

