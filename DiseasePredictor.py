# webapp using streamlit
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import datetime

# loading saved models

breast_cancer_model = pickle.load(open('Saved Models/breast_cancer_model.sav', 'rb'))

diabetes_model = pickle.load(open('Saved Models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('Saved Models/heart_disease_model.sav', 'rb'))

kidney_disease_model = pickle.load(open('Saved Models/kidney_disease.sav', 'rb'))

covid_disease_model = pickle.load(open('Saved Models/Covid19_model.sav', 'rb'))
# sidebar

with st.sidebar:
    select = option_menu('Disease Prediction Systems',
                         ['Home',
                          'Covid-19 Disease Prediction',
                          'Breast Cancer Prediction',
                          'Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Kidney Disease Prediction',
                          'Our Services'
                          ],

                         icons=['house','activity', 'activity', 'person', 'heart', 'activity', 'gear'],

                         default_index=0)

# pages
if select == 'Home':
    st.title('Welcome to disease predictor')
    st.write('')
    st.write('This website will help you to predict whether you are on the verge of developing a particular diesase'
             'or not')
    st.write('We use different algorithms to predict likelihood of developing disease using patient history and '
             'treatment data')
    st.write('You can directly book appointment through our website if you find you are prone to some disease')

    st.write('Even though this predictor is decently accurate we still intimate you not to completely rely on this')

    st.write('Have a nice and healthy day ♥')
if select == 'Breast Cancer Prediction':
    st.title('Breast Cancer Prediction using Machine Learning')

    radius_mean = st.text_input('Enter radius mean')
    texture_mean = st.text_input('Enter texture mean')
    perimeter_mean = st.text_input('Enter perimeter mean')
    area_mean = st.text_input('Enter area mean')
    smoothness_mean = st.text_input('Enter smoothness mean')
    compactness_mean = st.text_input('Enter compactness mean')
    concavity_mean = st.text_input('Enter concavity mean')
    concave_points_mean = st.text_input('Enter concave points mean')
    symmetry_mean = st.text_input('Enter symmetry mean')
    fractal_dimension_mean = st.text_input('Enter fractal dimension mean')

    radius_se = st.text_input('Enter radius se')
    texture_se = st.text_input('Enter texture se')
    perimeter_se = st.text_input('Enter perimeter se')
    area_se = st.text_input('Enter area se')
    smoothness_se = st.text_input('Enter smoothness se')
    compactness_se = st.text_input('Enter compactness se')
    concavity_se = st.text_input('Enter concavity se')
    concave_points_se = st.text_input('Enter concave points se')
    symmetry_se = st.text_input('Enter symmetry se')
    fractal_dimension_se = st.text_input('Enter fractal dimension se')

    radius_worst = st.text_input('Enter radius worst')
    texture_worst = st.text_input('Enter texture worst')
    perimeter_worst = st.text_input('Enter perimeter worst')
    area_worst = st.text_input('Enter area worst')
    smoothness_worst = st.text_input('Enter smoothness worst')
    compactness_worst = st.text_input('Enter compactness worst')
    concavity_worst = st.text_input('Enter concavity worst')
    concave_points_worst = st.text_input('Enter concave points worst')
    symmetry_worst = st.text_input('Enter symmetry worst')
    fractal_dimension_worst = st.text_input('Enter fractal dimension worst')

    breast_cancer_diag = ' '

    if st.button('Breast Cancer Test Result'):
        breast_cancer_prediction = breast_cancer_model.predict([[radius_mean, texture_mean, perimeter_mean,
                                                                 area_mean, smoothness_mean, compactness_mean,
                                                                 concavity_mean,
                                                                 concave_points_mean, symmetry_mean,
                                                                 fractal_dimension_mean, radius_se,
                                                                 texture_se, perimeter_se, area_se, smoothness_se,
                                                                 compactness_se,
                                                                 concavity_se, concave_points_se, symmetry_se,
                                                                 fractal_dimension_se,
                                                                 radius_worst, texture_worst, perimeter_worst,
                                                                 area_worst, smoothness_worst,
                                                                 compactness_worst, concavity_worst,
                                                                 concave_points_worst, symmetry_worst,
                                                                 fractal_dimension_worst]])
        if breast_cancer_prediction[0] == 1:
            breast_cancer_diag = 'Patient has breast cancer'

        else:
            breast_cancer_diag = 'Patient does not have breast cancer'

        st.success(breast_cancer_diag)

if select == 'Diabetes Prediction':
    st.title('Diabetes Prediction using Machine Learning')

    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Enter Glucose')
    BloodPressure = st.text_input('Enter blood pressure')
    SkinThickness = st.text_input('Enter Skin Thickness')
    Insulin = st.text_input('Enter insulin')
    BMI = st.text_input('Enter BMI')
    DiabetesPedigreeFunction = st.text_input('Enter Diabetes Pedigree Function')
    Age = st.text_input('Enter Age')
    Skin = st.text_input('Enter Skin')

    diab_diagnosis = ' '

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness

                                                      , Insulin, BMI, DiabetesPedigreeFunction, Age, Skin]])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'Patient Has Diabetes'

        else:
            diab_diagnosis = 'Patient Does Not Have Diabetes'

        st.success(diab_diagnosis)

if select == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using Machine Learning')

    Age1 = st.text_input('Enter Age')
    Sex = st.text_input('Enter Sex')
    Cp = st.text_input('Enter Cp')
    Trestbps = st.text_input('Enter TrestBps')
    Chol = st.text_input('Enter Chol')
    fbs = st.text_input('Enter FBS')
    Restecg = st.text_input('Enter Restcg')
    Thalach = st.text_input('Enter Thalach')
    Exang = st.text_input('Enter Exang')
    Oldpeak = st.text_input('Enter Oldpeak')
    Slope = st.text_input('Enter Slope')
    Ca = st.text_input('Enter Ca')
    Thal = st.text_input('Enter thal')

    heart_diag = ' '

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict(
            [[Age1, Sex, Cp, Trestbps, Chol, fbs, Restecg, Thalach, Exang, Oldpeak, Slope, Ca, Thal]])

        if heart_prediction[0] == 1:
            heart_diag = 'Patient has heart disease'

        else:
            heart_diag = 'Patient does not have heart disease'

        st.success(heart_diag)

if select == 'Kidney Disease Prediction':
    st.title('Kidney Disease Prediction using Machine Learning')

    Bp = st.text_input('Enter Bp')
    Sp = st.text_input('Enter Sp')
    Al = st.text_input('Enter Al')
    Su = st.text_input('Enter Su')
    Rbc = st.text_input('Enter RBC')
    Bu = st.text_input('Enter Bu')
    Sc = st.text_input('Enter Sc')
    Sod = st.text_input('Enter Sod')
    Pot = st.text_input('Enter Pot')
    Hemo = st.text_input('Enter Hemo')
    Wbcc = st.text_input('Enter Wbcc')
    Rbcc = st.text_input('Enter Rbcc')
    Htn = st.text_input('Enter Htn')

    kidney_diag = ' '

    if st.button('Kidney disease test result'):
        kidney_prediction = kidney_disease_model.predict(
            [[Bp, Sp, Al, Su, Rbc, Bu, Sc, Sod, Pot, Hemo, Wbcc, Rbcc, Htn]])

        if kidney_prediction[0] == 1:
            kidney_diag = 'Patient has kidney disease'

        else:
            kidney_diag = 'Patient does not have kidney disease'

        st.success(kidney_diag)

if select == 'Covid-19 Disease Prediction':
    st.title('Covid-19 Prediction using Machine Learning')

    Age = st.text_input('Enter Your Age')
    BodyTemp = st.text_input('Enter Your Body Temperature')
    Fatigue = st.radio('Do you feel fatigueness?',('Yes', 'No'))
    if Fatigue=='Yes':
        fatigue=1
    else:
        fatigue=0
    Cough = st.radio('Do you have cough?',('Yes', 'No'))
    if Cough=='Yes':
        cough=1
    else:
        cough=0
    BodyPain = st.radio('Do you feel body pain?',('Yes', 'No'))
    if BodyPain=='Yes':
        bodypain=1
    else:
        bodypain=0
    SoreThroat = st.radio('Do you have sore throat?',('Yes', 'No'))
    if SoreThroat=='Yes':
        sorethroat=1
    else:
        sorethroat=0
    BreathingDifficulty = st.radio('Do you feel difficulty in breathing?',('Yes', 'No'))
    if BreathingDifficulty=='Yes':
        breathingdifficulty=1
    else:
        breathingdifficulty=0

    covid_diag=' '

    if st.button('Covid19 Prediction Test Result'):
        covid_prediction = covid_disease_model.predict([[Age,BodyTemp,fatigue,cough,bodypain,sorethroat,breathingdifficulty]])

        if covid_prediction[0] == 1:
            covid_diag = 'Patient has Covid-19'

        else:
            covid_diag = 'Patient does not have Covid-19'

        st.success(covid_diag)

if select == 'Our Services':
    st.header(':blue[HOSPITALS IN YOUR AREA :]')

    with st.container():
        st.write("                                                ")
        image = Image.open('Screenshot 2023-01-30 165852.jpg')
        st.image(image, caption=None, width=400)
        st.write(':red[Dream Hospital]')
        st.write('It typically has a team of specialists from different medical disciplines, such as cardiology, oncology, neurology, orthopedics, gastroenterology, and others. The hospital may offer a range of services, including diagnostic tests, surgical procedures, and ongoing care for chronic conditions.')
        st.write('Address:- Shivaji Nagar,Pune,Maharashtra')
        st.write('Rating : 5☆☆☆☆☆ (2,400 users)')
        if st.button('Book Appointment'):
            form = st.form(key='Book Appointment')
            name = form.text_input('Enter your name :')
            age = form.text_input('Enter your age')
            sex = form.text_input('Enter your sex')
            phone_number = form.text_input('Enter your mobile number')
            email_address = form.text_input('Enter your email address')
            disease_type = form.text_input('Enter your disease')
            date_of_appointment = form.date_input('Enter Date for appointment')
            submit = form.form_submit_button('Submit')
            st.write('Press submit to have your name printed below')

            if submit:
                st.write(f'hello {name}')

    with st.container():
        image = Image.open('Screenshot 2023-01-30 165958.jpg')
        st.image(image, caption=None, width=400)
        st.write(':red[Chinook Hospital]')
        st.write('Specializes in diagnosing and treating heart and cardiovascular diseases. It typically has a team of cardiologists, cardiac surgeons, and other medical professionals trained in caring for patients with heart conditions.')
        st.write('Address:- Aundh,Pune,Maharashtra')
        st.write('Rating : 4 ☆☆☆☆ (500 users)')

        if st.button('Book Your Appointment'):
            form = st.form(key='Book Appointment')
            name = form.text_input('Enter your name :')
            age = form.text_input('Enter your age')
            sex = form.text_input('Enter your sex')
            phone_number = form.text_input('Enter your mobile number')
            email_address = form.text_input('Enter your email address')
            disease_type = form.text_input('Enter your disease')
            date_of_appointment = form.date_input('Enter Date for appointment')


            submit = form.form_submit_button('Submit')
            st.write('Press submit to have your name printed below')

            if submit:
                st.write(f'hello {name}')

    with st.container():
        image = Image.open('Screenshot 2023-01-30 170042.jpg')
        st.image(image, caption=None, width=400)
        st.write(':red[Siedman Cancer Hospital]')
        st.write('Specializes in the diagnosis, treatment, and care of cancer patients. It typically has a '
                 'multidisciplinary team of oncologists, radiation therapists, surgeons, nurses, and support staff '
                 'trained in caring for cancer patients.')
        st.write('Address:- Hadapsar,Pune,Maharashtra')
        st.write('Rating : 4☆☆☆☆ (1,200 users)')
        if st.button('Book An Appointment'):
            form = st.form(key='Book Appointment')
            name = form.text_input('Enter your name :')
            age = form.text_input('Enter your age')
            sex = form.text_input('Enter your sex')
            phone_number = form.text_input('Enter your mobile number')
            email_address = form.text_input('Enter your email address')
            disease_type = form.text_input('Enter your disease')
            date_of_appointment = form.date_input('Enter Date for appointment')


            submit = form.form_submit_button('Submit')
            st.write('Press submit to have your name printed below')

            if submit:
                st.write(f'hello {name}')














