from models import weather
import django_filters

class WeatherFilter(django_filters.FilterSet):
    class Meta:
        model = weather
        fields = ['date', 'apparent_temp', 'air_temp', ]