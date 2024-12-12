from flask import Flask, jsonify, request
import tensorflow as tf
import io
import pandas as pd
import numpy as np
from google.cloud import storage
from sqlalchemy import create_engine
from datetime import datetime, timedelta
import os
from utils import get_predictions

app = Flask(__name__)

# Koneksi ke database
engine = create_engine('mysql+pymysql://root:iniPunyaKu!@34.101.135.174:3306/prediksi')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Panggil fungsi untuk melakukan prediksi
        predictions = get_predictions(engine)  # Panggil fungsi dengan parameter engine
        return jsonify(predictions)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/getpredict', methods=['GET'])
def get_prediction_results():
    try:
        # Mengambil 2 data terakhir dari tabel predictions
        last_predictions = pd.read_sql('SELECT * FROM predictions ORDER BY prediction_date DESC LIMIT 2', engine)
        return jsonify(last_predictions.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))