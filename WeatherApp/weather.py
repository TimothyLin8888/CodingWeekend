import requests

api_key = open("WeatherApp/api_key.txt","r").read()

location = input("Location: ")

result = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}")

print(result.json()['coord']['lon'])

'''
{'coord': {'lon': -78.6386, 'lat': 35.7721}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 
'base': 'stations', 'main': {'temp': 20.8, 'feels_like': 20.01, 'temp_min': 19.6, 'temp_max': 22.29, 'pressure': 1031, 'humidity': 41, 
'sea_level': 1031, 'grnd_level': 1018}, 'visibility': 10000, 'wind': {'speed': 4.63, 'deg': 20, 'gust': 7.2}, 'clouds': {'all': 20}, 
'dt': 1729361129, 'sys': {'type': 2, 'id': 2042838, 'country': 'US', 'sunrise': 1729337094, 'sunset': 1729377217}, 'timezone': -14400, 
'id': 4487042, 'name': 'Raleigh', 'cod': 200}
'''