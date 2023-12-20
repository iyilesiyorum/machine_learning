import streamlit as st
import pandas as pd
import joblib

def get_brand_index(selected_brand):
    brand_dict = {'Xiaomi': 1, 'Apple': 2, 'Samsung': 3, 'Reeder': 4}
    return brand_dict[selected_brand]

def get_warranty_index(selected_warranty):
    warranty_dict = {'xiaomi garantili': 1, 'apple garantili': 2, 'samsung garantili': 3, 'resmi distrübitör': 4, 'genpa': 5}
    return warranty_dict[selected_warranty.lower()]

def run_app():
    st.title('Uygulamaya hoşgeldiniz.')

    # Marka seçimi (selectbox ile)
    selected_brand = st.selectbox("Marka Seçiniz", ["Xiaomi", "Apple", "Samsung", "Reeder"])
    selected_brand_index = get_brand_index(selected_brand)

    # Garanti seçimi (selectbox ile)
    selected_warranty = st.selectbox("Garanti Seçiniz", ["Xiaomi Garantili", "Apple Garantili", "Samsung Garantili", "Resmi Distrübitör", "Genpa"])
    selected_warranty_index = get_warranty_index(selected_warranty)

    # Dahili hafıza
    selected_memory = st.number_input("Dahili Hafıza (GB)", min_value=32, max_value=256)

    # Ön kamera çözünürlüğü
    selected_front_cam = st.slider("Ön Kamera Çözünürlüğü (MP)", min_value=8, max_value=50)

    # RAM kapasitesi
    selected_ram = st.number_input("RAM Kapasitesi (GB)", min_value=2, max_value=12)

    # Batarya kapasitesi
    selected_battery = st.slider("Batarya Kapasitesi (mAh)", min_value=750, max_value=5000)

    # Ekran boyutu
    selected_screenSize = st.slider("Ekran Boyutu (inç)", min_value=5.1, max_value=7.0)

    # Bağlantı hızı
    selected_connectionSpeed = st.radio("Bağlantı Hızı", ("4.5G", "5G"))

    # Modeli yükleme (dinamik dosya yolu)
    model_path = st.text_input("Model Dosya Yolu (isteğe bağlı)", value=r"C:\Users\hakan\source\repos\machine_learning\support_vector_machines.pkl")
    model = joblib.load(model_path)

    # Tahmin yapma
    features = [selected_memory, selected_front_cam, selected_ram, selected_battery, selected_screenSize, selected_connectionSpeed, selected_brand_index, selected_warranty_index]
    prediction = model.predict([features])

    # Tahmini fiyat
    st.write("Tahmini Fiyat:", prediction[0])

# Ana uygulama
run_app()
