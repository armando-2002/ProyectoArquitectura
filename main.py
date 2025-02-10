import requests
import os
import csv
from datetime import datetime

# Coordenadas de Bogotá
BOGOTA_LAT = 4.7110      # Latitud de Bogotá
BOGOTA_LONGITUDE = -74.0721  # Longitud de Bogotá
API_KEY = "70486714f925b9203d1f4018c9be6476"
FILE_NAME = "/home/joel/CityWeather/clima-bogota-hoy.csv"

def get_weather(lat, lon, api):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"cod": response.status_code}

def process(json_data):
    normalized_dict = {
        "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Temperatura": json_data["main"]["temp"],
        "Humedad": json_data["main"]["humidity"],
        "Presión": json_data["main"]["pressure"],
        "Velocidad del viento": json_data["wind"]["speed"],
        "dt": json_data.get("dt", "N/A"),
        "coord_lon": json_data["coord"].get("lon", "N/A"),
        "coord_lat": json_data["coord"].get("lat", "N/A"),
        "weather_0_id": json_data["weather"][0].get("id", "N/A"),
        "weather_0_main": json_data["weather"][0].get("main", "N/A"),
        "weather_0_description": json_data["weather"][0].get("description", "N/A"),
        "weather_0_icon": json_data["weather"][0].get("icon", "N/A"),
        "base": json_data.get("base", "N/A"),
        "main_temp": json_data["main"].get("temp", "N/A"),
        "main_feels_like": json_data["main"].get("feels_like", "N/A"),
        "visibility": json_data.get("visibility", "N/A"),
        "wind_speed": json_data["wind"].get("speed", "N/A"),
        "wind_deg": json_data["wind"].get("deg", "N/A"),
        "clouds_all": json_data.get("clouds", {}).get("all", "N/A"),
        "sys_type": json_data.get("sys", {}).get("type", "N/A"),
        "sys_id": json_data.get("sys", {}).get("id", "N/A"),
        "sys_country": json_data.get("sys", {}).get("country", "N/A"),
        "sys_sunrise": json_data.get("sys", {}).get("sunrise", "N/A"),
        "sys_sunset": json_data.get("sys", {}).get("sunset", "N/A"),
        "timezone": json_data.get("timezone", "N/A"),
        "id": json_data.get("id", "N/A"),
        "name": json_data.get("name", "N/A"),
        "cod": json_data.get("cod", "N/A"),
    }
    return normalized_dict

def write2csv(json_response, csv_filename):
    fieldnames = [
        "Fecha", "Temperatura", "Humedad", "Presión", "Velocidad del viento",
        "dt", "coord_lon", "coord_lat", "weather_0_id", "weather_0_main",
        "weather_0_description", "weather_0_icon", "base", "main_temp",
        "main_feels_like", "visibility", "wind_speed", "wind_deg",
        "clouds_all", "sys_type", "sys_id", "sys_country", "sys_sunrise",
        "sys_sunset", "timezone", "id", "name", "cod"
    ]
    
    file_exists = os.path.isfile(csv_filename)
    
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()
        
        writer.writerow(json_response)

def main():
    print("===== Bienvenido a Bogotá-Clima =====")
    bogota_weather = get_weather(lat=BOGOTA_LAT, lon=BOGOTA_LONGITUDE, api=API_KEY)
    
    if bogota_weather.get('cod') != 404:
        processed_weather = process(bogota_weather)
        write2csv(processed_weather, FILE_NAME)
        print("Datos climatológicos guardados correctamente en", FILE_NAME)
    else:
        print("Ciudad no disponible o API KEY no válida")

if __name__ == '__main__':
    main()
