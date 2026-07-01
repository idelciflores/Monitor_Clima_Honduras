import requests

def consultar_api(latitud, longitud):
    enlace = f"https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&current=temperature_2m,relative_humidity_2m,weather_code&hourly=temperature_2m"
    
    peticion = requests.get(enlace)
    if peticion.status_code == 200:
        return peticion.json()
    return None