from calendar import Calendar
from email.mime import image
from re import S
from sre_constants import SUCCESS
from click import option
import streamlit as st
import pandas as pd
from pathlib import Path

#Title text
st.write("# Hi, this is BlueSky's first web app!")
st.write("")
st.write("# EtherCAR RENTAL CAR! :smile:")
st.write("By BlueSky")

#Images import:
titleIMG = ("Streamlit_Resources/Title.PNG")
Por = ("Streamlit_Resources/911.jpeg")
Aventador = ("Streamlit_Resources/Aventador.jpeg")
C8 = ("Streamlit_Resources/C8.jpeg")
Dawn = ("Streamlit_Resources/Dawn.jpeg")
E350 = ("Streamlit_Resources/E350.jpeg")
G65 = ("Streamlit_Resources/G65.jpeg")
GTC = ("Streamlit_Resources/GTC.jpeg")
GTCS = ("Streamlit_Resources/GTCS.jpeg")
Huracan = ("Streamlit_Resources/Huracan.jpeg")
Deville = ("Streamlit_Resources/Deville.png")
RangeRover = ("Streamlit_Resources/RangeRover.png")
VanderHall = ("Streamlit_Resources/VanderHall.jpeg")
SUCCESSimg = ("Streamlit_Resources/Long_Road.jpg")

#Title IMG print
st.image(titleIMG)



#Price Chart import
Price1Chart = pd.read_csv(
    Path("Streamlit_Resources/PriceChart1.csv"),
    infer_datetime_format=False)
PriceChartDF = pd.DataFrame(Price1Chart)

#Price chart Print
#st.write(PriceChartDF)


# Choice conformation function. 
def GreatChoice():
    st.write("Great choice!")
    st.write(":sunglasses:")

#Car selection coice (user input)
st.write("# Pick your Car!")

#First row of colums created:
col1, col2, col3 = st.columns(3)

#First row of Colums layed out:
with col1:
    st.image(Por)
    if st.button("Book your 911!"):
        GreatChoice()

with col2:
    st.image(Aventador)
    if st.button("Book your Aventador!"):
        GreatChoice()


with col3:
    st.image(C8)
    if st.button("Book your C8!"):
        GreatChoice()

#Second row of columns created:
col4, col5, col6 = st.columns(3)

#Second row of columns layed out:
with col4:
    st.image(Dawn)
    if st.button("book your Dawn!"):
        GreatChoice()

with col5:
    st.image(E350)
    if st.button("Book your E350!"):
        GreatChoice()

with col6:
    st.image(G65)
    if st.button("Book your G65!"):
        GreatChoice()


#Third row of columns created:
col7, col8, col9 = st.columns(3)

#Third row of columns layed out:
with col7:
    st.image(GTC)
    if st.button("Book your GTC!"):
        GreatChoice()

with col8:
    st.image(GTCS)
    if st.button("Book your GTCS V8S!"):
        GreatChoice()

with col9:
    st.image(Huracan)
    if st.button("Book your Huracan"):
        GreatChoice()

#Fourth row of columns created:

col10, col11, col12 = st.columns(3)

with col10:
    st.image(RangeRover)
    if st.button("Book your Range Rover!"):
        GreatChoice()

with col11:
    st.image(VanderHall)
    if st.button("Book Your VanderHall!"):
        GreatChoice()

with col12:
    st.image(Deville)
    if st.button("Book your Deville now!"):
        GreatChoice()





#Sidebar selection

#Hours or days sidebar selection(User input)
Four_Twfr = ["4 Hours", "24 Hours"]
hours_amt = st.sidebar.selectbox("4 or 24 Hours?", Four_Twfr)


#Number of Hours or Days sidebar selection(user input)
number_of_H_R = st.sidebar.number_input("Number of 4 Hours/Days?")

#Day of Rental selection(user input)
calendar_input = st.sidebar.date_input("Please select your rental date: ",value=None, min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)

#Time of Rental Selection(user input)
time_input = st.sidebar.time_input("Please select your ", value=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)

#Rental book button!(User input)
if st.sidebar.button("Book your EtherCar!!"):
    st.sidebar.write("# Succsess!")
    st.sidebar.write("Thank your for using EtherCar!!")
    st.sidebar.write("Enjoy your trip! :sunglasses:")
    st.sidebar.balloons()
    st.sidebar.image(SUCCESSimg)