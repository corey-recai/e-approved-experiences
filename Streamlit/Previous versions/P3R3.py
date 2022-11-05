from click import option
import streamlit as st



import pandas as pd
from pathlib import Path

st.write("# EtherCAR RENTAL CAR!")
st.write("By BlueSky")


titleIMG = ("Streamlit_Resources/Title.PNG")
st.image(titleIMG)

st.write("# Hi, this is BlueSky's first web app! :sunglasses:")

#Price Chart import
Price1Chart = pd.read_csv(
    Path("Streamlit_Resources/PriceChart1.csv"),

    infer_datetime_format=False)
df = pd.DataFrame(Price1Chart)


st.write(df)

#Image Data

Mid_Size = ("Streamlit_Resources/mid.jpg")
lux = ("Streamlit_Resources/lux.jpg")
MiniVan = ("Streamlit_Resources/Mini.jpg")
Comp = ("Streamlit_Resources/COMP.jpg")




#Car selection
st.write("# Pick your Car!")

if st.button("Mid-Sized!"):
     st.image(Mid_Size)

if st.button("Compact Car!"):
    st.image(Comp)

if st.button("Luxary Car!"):
    st.image(lux)

if st.button("MiniVan"):
    st.image(MiniVan)