import requests
 
api_key = "6735deffdc93967779fbc6daedbe1594"
city = input("Hallo! Bitte gib eine Stadt ein. ")

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

data = requests.get(url).json()

temperatur = data['main']['temp']
feuchtigkeit = data['main']['humidity']

print(f'In {city} beträgt die Temperatur {temperatur}. Die Luftfeuchtigkeit beträgt {feuchtigkeit}')