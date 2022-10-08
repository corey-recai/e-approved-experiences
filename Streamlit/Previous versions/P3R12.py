from calendar import Calendar
from email.mime import image
from re import S
from click import option
import streamlit as st
import pandas as pd
from pathlib import Path


st.write("# Hi, this is BlueSkys first web app!:sunglasses:")
st.write("")
st.write("# EtherCAR RENTAL CAR!")
st.write("By BlueSky")

#Title IMG import
titleIMG = ("Streamlit_Resources/Title.PNG")

#Title IMG print
st.image(titleIMG)



#Price Chart import
Price1Chart = pd.read_csv(
    Path("Streamlit_Resources/PriceChart1.csv"),
    infer_datetime_format=False)
PriceChartDF = pd.DataFrame(Price1Chart)

#Price chart Print
#st.write(PriceChartDF)


#Image Data
Por = ("Streamlit_Resources/911.jpeg")
Aventador = ("Streamlit_Resources/Aventador.jpeg")
C8 = ("Streamlit_Resources/C8.jpeg")
Dawn = ("Streamlit_Resources/Dawn.jpeg")
E350 = ("Streamlit_Resources/E350.jpeg")
G65 = ("Streamlit_Resources/G65.jpeg")
GTC = ("Streamlit_Resources/GTC.jpeg")
GTCS = ("Streamlit_Resources/GTCS.jpeg")


# Choice conformation function. 
def GreatChoice():
    st.write("Great choice!")
    st.balloons()

#Car selection coice (user input)
st.write("# Pick your Car!")

st.image(Por)
if st.button("Book your 911!"):
    GreatChoice()

st.image(Aventador)
if st.button("Book your Aventador!"):
    GreatChoice()

st.image(C8)
if st.button("Book your C8!"):
    GreatChoice()

st.image(Dawn)
if st.button("book your Dawn!"):
    GreatChoice()

st.image(E350)
if st.button("Book your E350!"):
    GreatChoice()

st.image(G65)
if st.button("Book your G65!"):
    GreatChoice()

st.image(GTC)
if st.button("Book your GTC!"):
    GreatChoice()

st.image(GTCS)
if st.button("Book your GTCS!"):
    GreatChoice()






#Sidebar selection

#Hours or days sidebar selection(User input)
H_R = ["Hours", "Days"]
hours_days = st.sidebar.selectbox("Hours or Days?", H_R)


#Number of Hours or Days sidebar selection(user input)
number_of_H_R = st.sidebar.number_input("Number of Hours/Days?")

#Day of Rental selection(user input)
calendar_input = st.sidebar.date_input("Please select your rental date: ",value=None, min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)

#Time of Rental Selection(user input)
time_input = st.sidebar.time_input("Please select your ", value=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)

#Rental book button!(User input)
if st.sidebar.button("Book your EtherCar!!"):
    st.sidebar.write("Succsess!")
    st.sidebar.write("Thank your for using EtherCar!!")
    st.sidebar.write("Enjoy your trip!")