# planner/views.py

import openmeteo_requests
import requests_cache
from retry_requests import retry
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class WeatherAPIView(APIView):
    def get(self, request):
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')
        days = request.query_params.get('days', '7')  # Default to 7 days if not provided

        if not latitude or not longitude:
            return Response({"error": "Latitude and Longitude are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Setup the Open-Meteo API client with cache and retry on error
        cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
        retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
        openmeteo = openmeteo_requests.Client(session=retry_session)

        # Define the parameters for the API request
        params = {
            "latitude": float(latitude),
            "longitude": float(longitude),
            "hourly": "temperature_2m",
            "forecast_days": int(days)
        }

        try:
            # Make the request to the Open-Meteo API
            response = openmeteo.weather_api("https://api.open-meteo.com/v1/forecast", params=params)

            # Print the response object to debug its structure
            print(response)

            # Access the data based on the correct structure
            # Here, we assume `response` is an object; we'll need to inspect its structure
            # Adjust this part according to the printed output
            return Response({"message": "Check the server logs for response structure."}, status=status.HTTP_200_OK)

        except Exception as e:
            # Handle errors and return a 500 response
            return Response({"error": "Could not retrieve weather data.", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)