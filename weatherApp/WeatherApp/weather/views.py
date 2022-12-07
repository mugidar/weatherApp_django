import requests 
from django.shortcuts import render, HttpResponse
from .models import City
from .forms import CityForm

def index(request):
    appid = 'd949072338b463dae504c23a31f415f2'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid    
  
    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    
    cities = City.objects.all()
    
    all_cities = []
    for city in cities:
       
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city' : city.name,
            'temp' : res["main"]["temp"],
            'hum' : res["main"]["humidity"],
            'icon' : res["weather"][0]["icon"],
        }
        City.objects.filter(pk__in=City.objects.filter(name=city.name).values_list('id', flat=True)[1:]).delete()
        all_cities.append(city_info)
        
        
    context = {'all_info': all_cities, 'form' : form }
    
    return render(request, 'weather/index.html', context)