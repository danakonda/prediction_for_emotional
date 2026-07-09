import streamlit as st
import joblib

st.title("emotional based on prediction")
model=joblib.load("emotional.pkl")
vector=joblib.load("vector.pkl")
num=st.text_input("enter the text:")
if st.button("predict"):
    nums=vector.transform([num])
    pred=model.predict(nums)
    if pred==[1] :
        st.write("happy")
    elif pred==[2]:
        st.write("sad")
    else:
        st.write("nuetral")
    


