import pandas as pd
import numpy as np
from flask import Flask, url_for, request, render_template, Markup


from fertilizer import fertilizer_dic


# print(response)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Fertilizer_details.html')


@app.route('/fertilizers', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        crop_name = str(request.form['crop'])
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['pottasium'])
        # ph = float(request.form['ph'])

        df = pd.read_csv(r"E:\Projects\Smart_Harvest\fertilizer.csv")

        nr = df[df['Crop'] == crop_name]['N'].iloc[0]
        pr = df[df['Crop'] == crop_name]['P'].iloc[0]
        kr = df[df['Crop'] == crop_name]['K'].iloc[0]

        n = nr - N
        p = pr - P
        k = kr - K
        temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
        max_value = temp[max(temp.keys())]
        if max_value == "N":
            if n < 0:
                key = 'NHigh'
            else:
                key = "Nlow"
        elif max_value == "P":
            if p < 0:
                key = 'PHigh'
            else:
                key = "Plow"
        else:
            if k < 0:
                key = 'KHigh'
            else:
                key = "Klow"

        response = Markup(str(fertilizer_dic[key]))
        return render_template('Fertilizer_result.html', response = response)
    return render_template('Fertilizer_details.html')

if __name__ == '__main__':
    app.run(debug=True)