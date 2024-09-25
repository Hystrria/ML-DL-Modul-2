import streamlit as st
import pickle 
import os

model_path = 'GBT_HeartDisease_model.pkl'

with open(model,'rb') as f:
    loaded_model = pickle.load(f)

rf_model= loaded_model

st.title("Prediksi Potensi Penyakit Jantung")
st.write("Aplikasi ini berguna untuk membantu mengenali potensi penyakit jantung pada manusia berusia 21 - 79 tahun")
Age = st.slider("Age",21,79)
Sex = st.selectbox("Gender",["F","M"])
ChestPainType = st.selectbox("Chest Pain Type",["ASY","ATA","NAP","TA"])
RestingBP = st.number_input("Resting Blood Preassure",0,200)
Cholesterol = st.number_input("Cholesterol",0,603)
FastingBS = st.selectbox("Fasting BS",["1","0"])
RestingECG = st.selectbox("Resting ECG",["LVH","Normal","ST"])
MaxHR = st.number_input("Max Heart Rate",60,202)
ExcerciseAngina = st.radio("Excercise Angina",["N","Y"])
Old_peak = st.slider("Old Peak",-3.0,7.0,step=0.1)
ST_Slope=st.selectbox("ST_Slope",["Down","Flat","Up"])

if Sex == "F":
    input_sex_F = 1
    input_sex_M =0
elif Sex == "M":
    input_sex_F = 0
    input_sex_M = 1

if ChestPainType == "ASY":
    input_cpain_ASY = 1
    input_cpain_ATA = 0
    input_cpain_NAP = 0
    input_cpain_TA = 0
elif ChestPainType == "ATA":
    input_cpain_ASY = 0
    input_cpain_ATA = 1
    input_cpain_NAP = 0
    input_cpain_TA = 0
elif ChestPainType == "NAP":
    input_cpain_ASY = 0
    input_cpain_ATA = 0
    input_cpain_NAP = 1
    input_cpain_TA = 0
elif ChestPainType == "TA":
    input_cpain_ASY = 0
    input_cpain_ATA = 0
    input_cpain_NAP = 0
    input_cpain_TA = 1

if FastingBS == 0:
    input_fastbs = 0
else:
    input_fastbs = 1

if RestingECG == "LVH":
    input_restecg_LVH = 1
    input_restecg_NORMAL = 0
    input_restecg_ST = 0
elif RestingECG == "Normal":
    input_restecg_LVH = 0
    input_restecg_NORMAL = 1
    input_restecg_ST = 0
elif RestingECG == "ST":
    input_restecg_LVH = 0
    input_restecg_NORMAL = 0
    input_restecg_ST = 1

if ExcerciseAngina == ["Y"]:
    input_anginaY = 1
    input_anginaN = 0
else:
    input_anginaY = 0
    input_anginaN = 1

if ST_Slope == "Down":
    input_STslope_down = 1
    input_STslope_flat = 0
    input_STslope_up = 0
elif ST_Slope == "Flat":
    input_STslope_down = 0
    input_STslope_flat = 1
    input_STslope_up = 0
elif ST_Slope == "Up":
    input_STslope_down = 0
    input_STslope_flat = 0
    input_STslope_up = 1


input_data = [[input_sex_F,input_sex_M,input_cpain_ASY,
               input_cpain_ATA,input_cpain_NAP,input_cpain_TA,
               input_restecg_LVH,input_restecg_NORMAL,input_restecg_ST,
               input_anginaN,input_anginaY,input_STslope_down,
               input_STslope_flat,input_STslope_up,Age,
               RestingBP,Cholesterol,input_fastbs,MaxHR,Old_peak]]


st.write("Data pasien yang akan diinput ke model")
st.write(input_data)


if st.button("Prediksi"):
    rf_model_prediction = rf_model.predict(input_data)
    outcome= {0:'Tidak Berpotensi sakit jantung', 1:'Berpotensi sakit jantung'}
    st.write(f"Orang tersebut diprediksi **{outcome[rf_model_prediction[0]]}**")
