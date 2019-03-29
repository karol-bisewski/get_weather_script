import requests
import sys

url = 'https://api.openweathermap.org/data/2.5/weather'

# You need to get your own API key from: http://openweathermap.org/appid
key = ''

try:
    city = sys.argv[1]
except IndexError:
    script_name = sys.argv[0]
    print(f'usage: python {script_name} [city]')
    sys.exit(1)

try:
    response = requests.get(
        url=url,
        params=dict(q=city, APPID=key, units='metric'),
    )
except requests.exceptions.RequestException as e:
    print(e)
    sys.exit(1)

weather = response.json()

OK = (200 or '200')
if weather['cod'] != OK:
    print(weather['message'])
    sys.exit(1)
else:
    temperature = str(weather['main']['temp'])
    unit = '\u00B0C'
    print(f'{temperature}{unit}')
