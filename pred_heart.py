## import the libraries
import streamlit as st
import numpy as np
from PIL import Image
from tensorflow import keras

## load the ann model
model = keras.models.load_model("heart_disease.h5")

## create a function for prediction
def heart_prediction(input):
    input_array = np.asarray(input)
    input_reshape = input_array.reshape(1,-1)
    prediction = model.predict(input_reshape)
    print(prediction)

    if  (prediction[0] == 0):
        return 'You are likely to die from heart failure given your health condition'
    else:
        return 'You are not likely to die from heart failure given your health condition'
    
## Page Configuration       
def main():
    st.set_page_config(page_title="Heart Failure Predictor", layout="wide")

    ## add image
    image = Image.open('heart.png')
    st.image(image, use_column_width=False)
    # set title and content
    st.title('Heart Failure Predictor using Artificial Neural Network')
    st.write('Enter your personal data to get your heart risk evaluation')

    # get input from the user
    age = st.number_input('Age of the patient:', min_value=0, step=1)
    anaemia = st.number_input('Anaemia | Yes or No | yes = 1 and no = 0', min_value=0, step=1)
    creatinine_phosphokinase = st.number_input('Level of CPK enzyme in the blood (mcg/L)', min_value=0, step=1)
    diabetes = st.number_input('Diabetes | Yes or No | yes = 1 and no = 0', min_value=0, step=1)
    ejection_fraction = st.number_input('Percentage blood leaving the heart', min_value=0, step=1)
    high_blood_pressure = st.number_input('Hypertensive | Yes or No | yes = 1 and no = 0', min_value=0, step=1)
    platelets = st.number_input('Platelets count of blood (kiloplatelets/mL)', min_value=0, step=1)
    serum_creatinine = st.number_input('Level of serum creatinine in the blood (mg/dL)', min_value=0.00, step=0.01)
    serum_sodium = st.number_input('Level of serum sodium in the blood (mEq/L)', min_value=0, step=1)
    sex = st.number_input('Sex of the patient | Male or Female | female = 1 and male = 0', min_value=0, step=1)
    smoking = st.number_input('Smoking | Yes or No | yes = 1 and no = 0', min_value=0, step=1)
    time = st.number_input('Follow-up Period (days):', min_value=0, step=1)

    # code for prediction
    predict = ''
    # button for prediction
    if st.button('Predict'):
        predict = heart_prediction([age, 
                                    anaemia, 
                                    creatinine_phosphokinase, 
                                    diabetes, ejection_fraction, 
                                    high_blood_pressure, 
                                    platelets, 
                                    serum_creatinine, 
                                    serum_sodium, 
                                    sex, smoking, 
                                    time])
    st.success(predict)

if __name__ == '__main__':
    main()




## python -m 
