from django.shortcuts import render
import requests
import json


def home(request):
    response = requests.get("http://api.ipstack.com/check?access_key=f7d722b02af8b6d1c7eacf4f4bbd86a2")
    geodata = response.json()
    return render(request, 'home.html', {
        'ip': geodata['ip'],
        'country': geodata["country_name"],
        'latitude': geodata["latitude"],
        'longitude': geodata["longitude"],
        'api_key': 'AIzaSyDCO9H3dVdsRJrSRrM77CYtKZTUl9ZqBzw'  # Don't do this! This is just an example. Secure your keys properly.
        })

def github(request):
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        user = response.json()
    return render(request, 'github.html', {'user': user})
