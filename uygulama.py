import streamlit as st
import pandas as pd
import joblib

def get_garanti_index(selected_garanti):
    garanti_dict = {'xiaomi garantili': 1, 'apple garantili': 2, 'samsung garantili': 3, 'resmi distr�bit�r': 4, 'genpa': 5}
    return garanti_dict[selected_garanti.lower()]  # K���k harfe �evirerek e�le�meyi sa�la

def get_marka_index(selected_marka):
    marka_dict = {'Xiaomi': 1, 'Apple': 2, 'Samsung': 3, 'Reeder': 4}
    return marka_dict[selected_marka]

def run_app():
    st.title('Uygulamaya ho�geldiniz.')

    # Kullan�c� marka se�imini yapmadan �nce hangi say�n�n hangi markaya denk geldi�ini belirtelim
    st.write("1: Xiaomi")
    st.write("2: Apple")
    st.write("3: Samsung")
    st.write("4: Reeder")

    # Kullan�c� marka se�imini butonlar arac�l���yla yaps�n
    selected_marka = st.button('Xiaomi')
    selected_brand = get_marka_index('Xiaomi') if selected_marka else None

    selected_marka = st.button('Apple')
    selected_brand = get_marka_index('Apple') if selected_marka else None

    selected_marka = st.button('Samsung')
    selected_brand = get_marka_index('Samsung') if selected_marka else None

    selected_marka = st.button('Reeder')
    selected_brand = get_marka_index('Reeder') if selected_marka else None

    # Kullan�c� garanti t�r� se�imini yapmadan �nce hangi say�n�n hangi garanti t�r�ne denk geldi�ini belirtelim
    st.write("1: Xiaomi Garantili")
    st.write("2: Apple Garantili")
    st.write("3: Samsung Garantili")
    st.write("4: Resmi Distr�bit�r")
    st.write("5: Genpa")

    # Kullan�c� garanti t�r� se�imini butonlar arac�l���yla yaps�n
    selected_garanti_xiaomi = st.button('Xiaomi Garantili')
    selected_garanti = get_garanti_index('xiaomi garantili') if selected_garanti_xiaomi else None

    selected_garanti_apple = st.button('Apple Garantili')
    selected_garanti = get_garanti_index('apple garantili') if selected_garanti_apple else None

    selected_garanti_samsung = st.button('Samsung Garantili')
    selected_garanti = get_garanti_index('samsung garantili') if selected_garanti_samsung else None

    selected_garanti_resmi = st.button('Resmi Distr�bit�r')
    selected_garanti = get_garanti_index('resmi distr�bit�r') if selected_garanti_resmi else None

    selected_garanti_genpa = st.button('Genpa')
    selected_garanti = get_garanti_index('genpa') if selected_garanti_genpa else None

    selected_memory = st.number_input('Dahili Haf�za', min_value=32, max_value=256)
    st.write("Dahili Haf�za:" + str(selected_memory) + "GB")

    selected_front_cam = st.slider("�n Kamera ��z�n�rl���:", min_value=8, max_value=50)
    st.write("�n Kamera ��z�n�rl���:" + str(selected_front_cam) + "MP")

    selected_ram = st.number_input("RAM Kapasitesi", min_value=2, max_value=12)
    st.write("RAM Kapasitesi:" + str(selected_ram) + "GB")

    selected_battery = st.slider("Batarya Kapasitesi", min_value=750, max_value=5000)
    st.write("Batarya Kapasitesi" + str(selected_battery) + "mAh")

    selected_screenSize = st.slider("Ekran Boyutu", min_value=5.1, max_value=7.0)
    
    selected_connectionSpeed = st.radio("Ba�lant� H�z�", ('4.5G', '5G'))

    # Modeli y�kleme ve tahmin yapma
    model = joblib.load("support_vector_machines.pkl")
    features = [selected_memory, selected_front_cam, selected_ram, selected_battery, selected_screenSize, selected_connectionSpeed, selected_brand, selected_garanti]
    prediction = model.predict([features])

    st.write("Tahmini Fiyat:", prediction[0])

# Ana uygulama
run_app()
