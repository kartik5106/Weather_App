import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    city = "mangalore"
    myApi= '05c506850f2a4c7f868101120231309'
    url =f'http://api.weatherapi.com/v1/current.json?key={myApi}&q={city}&aqi=no'
    r = requests.get(url).json()
    
    city_weather = {
        'city': city,
        'temperature': r['current']['temp_c'],
        'description':r['current']['condition']['text']
    }
    context = {'city_weather' : city_weather}
    return render(request,'sample.html',context)
