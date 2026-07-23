{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "33f0e4cf-e1d1-4a18-bf8d-4becdf822f39",
   "metadata": {},
   "outputs": [],
   "source": [
    "def generate_weather_response(data):\n",
    "    \"\"\"\n",
    "    data = {\n",
    "        'city': 'London',\n",
    "        'temp': 18,\n",
    "        'condition': 'sunny',\n",
    "        'humidity': 65,\n",
    "        'wind_speed': 12\n",
    "    }\n",
    "    \"\"\"\n",
    "    return f\"\"\"🌤️ Weather Report for {data['city']}\n",
    "    return f\"\"\"🌤️ Weather Report for {data['city']}\n",
    "\n",
    "Temperature: {data['temp']}°C\n",
    "Condition: {data['condition']}\n",
    "Humidity: {data['humidity']}%\n",
    "Wind Speed: {data['wind_speed']} km/h\n",
    "\n",
    "{'☀️' if data['condition'] == 'sunny' else '☁️' if data['condition'] == 'cloudy' else '🌧️'} Enjoy your day!\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8522f596-f6cc-4b80-8a15-76e01c1bce1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "weather_data = {\n",
    "    'city': 'London',\n",
    "    'temp': 18,\n",
    "    'condition': 'sunny',\n",
    "    'humidity': 65,\n",
    "    'wind_speed': 12\n",
    "}\n",
    "\n",
    "print(generate_weather_response(weather_data))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
