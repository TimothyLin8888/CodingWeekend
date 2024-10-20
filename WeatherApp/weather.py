import requests

def get_wind_direction(wind_degree):
    directions = {
        "North-North-East": (22.5, 67.5),
        "East": (67.5, 112.5),
        "South-East": (112.5, 157.5),
        "South": (157.5, 202.5),
        "South-West": (202.5, 247.5),
        "West": (247.5, 292.5),
        "North-West": (292.5, 337.5),
        "North": (337.5, 360)
    }
    if 0 <= wind_degree < 22.5:
        return "North"
    for direction, (low, high) in directions.items():
        if low <= wind_degree < high:
            return direction

    return "Unknown"

api_key = open("WeatherApp/api_key.txt","r").read()

location = input("Location: ")

result = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}")

while True:
    print("1) Get the coordinates\n2) Get the weather and temperature\n3) Wind Speed")
    input_num = int(input("What would you like: "))
    match input_num:
        case 1:
            print(f"Longitude: {result.json()['coord']['lon']}")
            print(f"Latitude:  {result.json()['coord']['lat']}")
            input("Enter to continue: ")
            continue
        case 2:
            degree = input("F or C: ")
            multiply = 1
            add = 0
            if degree.lower() == 'f':
                multiply = 9/5
                add = 32
            print(f"Temperature: {(result.json()['main']['temp'] * multiply) + add:.2f}")
            print(f"Feels Like:  {(result.json()['main']['feels_like']* multiply) + add:.2f}")
            print(f"Max Temp:    {(result.json()['main']['temp_max']* multiply) + add:.2f}")
            print(f"Min Temp:    {(result.json()['main']['temp_min']* multiply) + add:.2f}")
            print(f"Humidity:    {result.json()['main']['humidity']}")
            input("Enter to continue: ")
            continue
        case 3:
            wind_degree = result.json()['wind']['deg']
            print(f"Wind Speed:   {result.json()['wind']['speed']}")
            print(f"Wind Degree:  {result.json()['wind']['deg']}")
            print(f"Direction:    {get_wind_direction(wind_degree)}")
            input("Enter to continue: ")
            continue
        case 4:
            break
'''
{
'coord': {'lon': -78.6386, 'lat': 35.7721}, 
'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 
'base': 'stations', 
'main': {'temp': 20.8, 'feels_like': 20.01, 'temp_min': 19.6, 'temp_max': 22.29, 'pressure': 1031, 'humidity': 41, 
'sea_level': 1031, 'grnd_level': 1018}, 
'visibility': 10000, 
'wind': {'speed': 4.63, 'deg': 20, 'gust': 7.2}, 
'clouds': {'all': 20}, 
'dt': 1729361129, 
'sys': {'type': 2, 'id': 2042838, 'country': 'US', 'sunrise': 1729337094, 'sunset': 1729377217}, 
'timezone': -14400, 
'id': 4487042, 
'name': 'Raleigh', 
'cod': 200
}
'''