import tensorflow as tf
import pandas as pd
import numpy as np
import math
from sklearn.metrics import mean_absolute_error, mean_squared_error
from tensorflow import keras
from tensorflow.keras.layers import Input, LSTM, Dense, Dropout, Flatten
from sqlalchemy import create_engine
import pymysql  # Untuk koneksi MySQL
import google.cloud.storage 
from datetime import datetime

def get_predictions(engine):  # Tambahkan parameter engine
    # Mengambil data dari tabel di database
    df = pd.read_sql('SELECT * FROM data_harga', engine)

    week = np.array(df["3 Hari"])
    series = np.array(df['Harga/3 hari'])

    window_size = 24

    def scaled_price(data):
        return data / 1000

    def inverse_scale(data):
        return data * 1000

    # Mengambil model dari bucket di cloud storage
    loaded_model = tf.keras.models.load_model('gs://ml-strg/model_prediksi_3hari.keras')

    print(loaded_model.input_shape)
    actual = series[-24:]
    seq_res = np.array([])
    act_temp = actual.reshape(-1, 1)

    actual_scaled = scaled_price(act_temp)
    seq = actual_scaled[-window_size:]

    # Melakukan prediksi dua kali
    for _ in range(2):
        hasil = loaded_model.predict(seq.reshape(1, window_size, 1))
        hasil = inverse_scale(hasil)
        seq_res = np.append(seq_res, hasil.item())
        act_temp = np.append(act_temp, np.expand_dims([hasil.item()], axis=1))

        actual_scaled = scaled_price(act_temp)
        seq = actual_scaled[-window_size:]

    # Menyimpan hasil prediksi ke tabel predictions di database
    predictions_df = pd.DataFrame({
        'commodity': ['Bawang'] * len(seq_res),  # Ganti 'commodity_name' dengan nama komoditas yang sesuai
        'prediction_date': [datetime.now().date()] * len(seq_res),
        'predicted_price': seq_res
    })
    print('Predict berhasil, sudah tersimpan di database')
    predictions_df.to_sql('predictions', engine, if_exists='append', index=False)