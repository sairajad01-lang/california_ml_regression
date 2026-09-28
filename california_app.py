import numpy as np
import streamlit as st
import joblib

obj=joblib.load('california.joblib')
model=obj['model']
columns=obj['columns']

#---------------------------------Columns
st.title('California Model')
In=[]
for i in columns:
    v=st.number_input(f'Enter the {i} value:')
    In.append(v)

#-------------------------------------Button
if st.button('Submit'):
    
    out=model.predict([In])
    st.success(f'The midhouse vali is:{out}')

