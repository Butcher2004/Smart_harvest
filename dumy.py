#To know the zipcode latitudes and longitudes

import requests
import json
from flask import Flask, render_template, url_for, request




app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        zip_code = request.form['zip']
        api_key = "56765cc0691fe16b12cf69c42ce61c10"

        headers = {
            "apikey": "90c125c0-e455-11ee-aee3-13a3b378e2b5"}

        params = (
            ("codes", zip_code),
        )

        response = requests.get('https://app.zipcodebase.com/api/v1/search', headers=headers, params=params);

        response = json.loads(response.text)
        results = response['results'][zip_code]
        latitude = results[0]['latitude']
        longitude = results[0]['longitude']

        # using Latitude and Longitude
        resp = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}")


        data = json.loads(resp.text)

        # Extract temperature, humidity, longitude, and latitude
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        longitude = data['coord']['lon']
        latitude = data['coord']['lat']
        state = results[0]['state']
        province = results[0]['province']
        print("Tempeeeeeee", temperature, humidity)
        return render_template('index.html', temperature=temperature, humidity=humidity, longitude=longitude, latitude=latitude, state=state, province=province)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)