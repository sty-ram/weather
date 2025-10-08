# from flask import Blueprint, render_template, request
# import requests
# from flask_login import login_required
# import os

# weather_bp = Blueprint('weather', __name__)

# API_KEY=os.get.env("API_KEY_W")
# @weather_bp.route('/weather', methods=['GET', 'POST'])
# @login_required
# def weather():
#     weather_data = None
#     if request.method == 'POST':
#         city = request.form['city']
#         url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
#         #url =f"https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
#         response = requests.get(url)
#         if response.status_code == 200:
#             data = response.json()
#             weather_data = {
#                 'city': data['name'],
#                 'temperature': data['main']['temp'],
#                 'description': data['weather'][0]['description'],
#             }
#         else:
#             weather_data = {'error': 'City not found.'}
#     return render_template('weather.html', weather=weather_data)
from flask import Blueprint, render_template, request, current_app
import requests
from flask_login import login_required

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/weather', methods=['GET', 'POST'])
@login_required
def weather():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        api_key = current_app.config.get('OPENWEATHERMAP_API_KEY')

        if not api_key:
            weather_data = {'error': 'API key not configured properly.'}
        else:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': data['name'],
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                }
            else:
                weather_data = {'error': 'City not found.'}

    return render_template('weather.html', weather=weather_data)
