#%%

from flask import Blueprint, request, jsonify
import requests

itineraries_bp = Blueprint('itineraries', __name__)

@itineraries_bp.route('/create', methods=['POST'])
def create_itinerary():
    data = request.get_json()
    # Aquí puedes procesar los datos del itinerario
    return jsonify({"message": "Itinerario creado con éxito"}), 201

@itineraries_bp.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    api_key = 'tu_clave_de_api_de_openweathermap'
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
    weather = response.json()
    return jsonify(weather)

@itineraries_bp.route('/country', methods=['GET'])
def get_country():
    country_name = request.args.get('country')
    response = requests.get(f'https://restcountries.com/v3.1/name/{country_name}')
    country = response.json()
    return jsonify(country)