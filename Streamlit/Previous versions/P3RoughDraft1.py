from click import option
import streamlit as st



import pandas as pd
from pathlib import Path

st.write("# INSTA CAR!")

#st.write("# Hi, this is our first web app in Python! :sunglasses:")

KAWASAKI_CSV = pd.read_csv(
    Path("KAWA_SAMPLE_CSV.CSV"),
    infer_datetime_format=False)
df = pd.DataFrame(KAWASAKI_CSV)

#KAWI_JET_SKI = pd.read_csv(
    Path("Jet_ski_samp.csv"),
    infer_datetime_format=False
#)
#Jet_DF = pd.DataFrame(KAWI_JET_SKI)

#Street_Bike_price_list = ("KAWI_PIC_TEST_1.PNG")
#Dual_sport = ("KAWI_PIC_TEST_2.PNG")

#st.write("Dealer Price list")
#price_list = st.image("KAWI_PIC_TEST_1.PNG")
st.write("PRICE LIST")
if st.button("Kawasaki Street Bike Price List"):
     st.image(Street_Bike_price_list)
if st.button("Kawasaki Dual sport"):
    st.image(Dual_sport)


#Street_Bike = print(df)
#Jet_Ski = print(Jet_DF)
#st.write(df)
#st.write(Jet_DF)
#st.multiselect("Please select a powersports class",options= ["Street Bike", "Jet Ski"])

#for st.multiselect in options:
    #if options == "Street Bike":
        #st.write(df),
        #Street_Bike
    #if options == "Jet Ski":
        #st.write(Jet_DF),
        #Jet_Ski



#input_value = st.text_input("Enter a Message")
st.write("ORDER BOARD")
if st.button("Kawasaki Street Bike"):
     st.write(df)
if st.button("Kawasaki Jet Ski"):
    st.write(Jet_DF)    