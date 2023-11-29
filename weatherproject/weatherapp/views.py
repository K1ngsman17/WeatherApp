from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Kochi'

    api_key = 'fe7457af54dd537c579a4ca1a33d0c51'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    params = {'units': 'metric'}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()

        return render(request, 'weatherapp/index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
            'invalid_city': False
        })
    
    else:
        messages.error(request, 'Data for entered City is not available with the API')
        day = datetime.date.today()
        return render(request, 'weatherapp/index.html', {
            'description': '',
            'icon': '',
            'temp': '',
            'day': day,
            'city': city,
            'invalid_city': True
        })