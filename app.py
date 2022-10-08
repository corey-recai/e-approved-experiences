import json
from web3 import Web3, HTTPProvider
from calendar import Calendar
from email.mime import image
from re import S
from sre_constants import SUCCESS
from click import option
import streamlit as st
import pandas as pd
from pathlib import Path


# truffle development blockchain address
blockchain_address = 'HTTP://127.0.0.1:7545'


# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))


# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]


# Path to the compiled contract JSON file
compiled_contract_path = 'build/contracts/Rental.json'

#Compiled_contract_path_forTotal = 'build/contracts/RentalSystem.json'

# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0x01aA9a6693530903D3d63a8447731D31c56ae4Ad'


with open(compiled_contract_path) as file:
    contract_json = json.load(file)  # load contract info as JSON
    # fetch contract's abi - necessary to call its functions
    contract_abi = contract_json['abi']

#with open(Compiled_contract_path_forTotal) as file:
    #contract_json = json.load(file)
    #contract_abiTotal = contract_json['abi']

# Fetch deployed contract reference
contract = web3.eth.contract(
    address=deployed_contract_address, abi=contract_abi)


# Call contract function (this is not persisted to the blockchain)
message = contract.functions.getCarCount().transact()


print(message)
# print(message[0])
# print(int.from_bytes(message, "big"))

#TEST adress :
_to = 0x4AC45fAA82B0B53aB8AE430FdA675E8f0F40d228

##STREAMLIT UI###

# Title text
st.write("# Hi, this is BlueSky's first web app!")
st.write("")
st.write("# EtherCAR RENTAL CAR! :smile:")
st.write("By BlueSky")

# Images import:
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
VanderHall = ("Streamlit_Resources/Vanderhall.jpeg")
SideBarTop = ("Streamlit_Resources/Sidebar_top.png")
SUCCESSimg = ("Streamlit_Resources/Long_Road.jpg")

# Title IMG print
st.image(titleIMG)



#SESSION STATE DEFULT VALUES. 
Hourly = 0
Daily = 0
carId = 0
# Hour price Streamlit session state test. 
if 'Hourly' not in st.session_state:
    st.session_state['Hourly'] = 0



# Choice conformation function.
def GreatChoice():
    #HH = Hourly * 4
    st.write("Four Hour Rate", Hourly)
    st.write("Daily Rate", Daily)
    st.sidebar.write("# Great choice!:sunglasses:")
    st.sidebar.write("# Please enter your Ethercar Duration & Date bellow :arrow_down:")

# Streamlit session state for carId


def getRental():
    st.sidebar.write(car.getId())
    msg.sender.transfer(Total)
    return contract.functions.rent(car.getId()).transact()

class Car:
  #def __init__(self):
    #self.carId = 0

  def setId(self, id):
    self.carId = id
    print(self.carId)
  def getId(self):
    return self.carId
car = Car()

def passPrice():
    st.sidebar.write(Total._value)
    return contract.functions.transfer(Total.getVal()).transact(0x4AC45fAA82B0B53aB8AE430FdA675E8f0F40d228, 1000000)

class Total:
    
    def setTotal(self, tab):
        self._value = tab
        print(self._value)
    def getVal(self):
        return self._value
Total = Total()




# Four Hour Streamlit session state  

if 'FOURHOUR' not in st.session_state:
    st.session_state["FOURHOUR"] = 0 


# Daily streamlit session state.

if 'Daily' not in st.session_state:
    st.session_state['Daily'] = 0

if 'hours_amt' not in st.session_state:
    st.session_state['hours_amt'] = 4


#Modle number streamlit session state. 
if 'MOD' not in st.session_state:
    st.session_state['MOD'] = 0 

# Car selection coice (user input)

st.write("# Pick your Car!")


# Car Data dictinary created.

CarData = {'MOD': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
           'HOURLY': [112.50, 250, 100, 199.75, 50, 112.50, 99.75, 99.75, 150, 100, 87.25, 50],
           'FOURHOUR' : [449.99, 999.99, 399,99, 799.00, 199.99, 449.99, 399.99, 399.99, 599.99, 349.99, 249.99, 399.99],
           'DAY': [999, 1999.99, 599.99, 1199, 249, 699, 699, 599, 1199, 475, 249.99, 599.99]
           }

HH = CarData["DAY"][3]
# First row of colums created:
col1, col2, col3 = st.columns(3)

# First row of Colums layed out:
with col1:
    st.image(Por)
    if st.button("Book your 911!"):
        car.setId(1)
        ModleID = CarData['MOD'][0]
        Hourly = CarData['FOURHOUR'][0]
        Daily = CarData['DAY'][0]
        GreatChoice()


with col2:
    st.image(Aventador)
    if st.button("Book your Aventador!"):
        car.setId(2)
        ModleID = CarData['MOD'][1]
        Hourly = CarData['FOURHOUR'][1]
        Daily = CarData['DAY'][1]
        GreatChoice()


with col3:
    st.image(C8)
    if st.button("Book your C8!"):
        car.setId(3)
        ModleID = CarData['MOD'][2]
        Hourly = CarData['FOURHOUR'][2]
        Daily = CarData['DAY'][2]
        GreatChoice()

# Second row of columns created:
col4, col5, col6 = st.columns(3)

# Second row of columns layed out:
with col4:
    st.image(Dawn)
    if st.button("book your Dawn!"):
        car.setId(4)
        ModleID = CarData['MOD'][3]
        Hourly = CarData['FOURHOUR'][3]
        Daily = CarData['DAY'][3]
        GreatChoice()

with col5:
    st.image(E350)
    if st.button("Book your E350!"):
        car.setId(5)
        ModleID = CarData['MOD'][4]
        Hourly = CarData['FOURHOUR'][4]
        Daily = CarData['DAY'][4]
        GreatChoice()

with col6:
    st.image(G65)
    if st.button("Book your G65!"):
        car.setId(6)
        ModleID = CarData['MOD'][5]
        Hourly = CarData['FOURHOUR'][5]
        Daily = CarData['DAY'][5]
        GreatChoice()


# Third row of columns created:
col7, col8, col9 = st.columns(3)

# Third row of columns layed out:
with col7:
    st.image(GTC)
    if st.button("Book your GTC!"):
        car.setId(7)
        ModleID = CarData['MOD'][6]
        Hourly = CarData['FOURHOUR'][6]
        Daily = CarData['DAY'][6]
        GreatChoice()

with col8:
    st.image(GTCS)
    if st.button("Book your GTCS V8S!"):
        car.setId(8)
        ModleID = CarData['MOD'][7]
        Hourly = CarData['FOURHOUR'][7]
        Daily = CarData['DAY'][7]
        GreatChoice()

with col9:
    st.image(Huracan)
    if st.button("Book your Huracan"):
        car.setId(9)
        ModleID = CarData['MOD'][8]
        Hourly = CarData['FOURHOUR'][8]
        Daily = CarData['DAY'][8]
        GreatChoice()

# Fourth row of columns created:

col10, col11, col12 = st.columns(3)

with col10:
    st.image(RangeRover)
    if st.button("Book your Range Rover!"):
        car.setId(10)
        ModleID = CarData['MOD'][9]
        Hourly = CarData['FOURHOUR'][9]
        Daily = CarData['DAY'][9]
        GreatChoice()

with col11:
    st.image(VanderHall)
    if st.button("Book Your VanderHall!"):
        car.setId(11)
        ModleID = CarData['MOD'][10]
        Hourly =  CarData['FOURHOUR'][10]
        Daily = CarData['DAY'][10]
        GreatChoice()

with col12:
    st.image(Deville)
    if st.button("Book your Deville now!"):
        car.setId(12)
        ModleID = CarData['MOD'][11]
        Hourly =  CarData['FOURHOUR'][11]
        Daily = CarData['DAY'][11]
        GreatChoice()






# Sidebar image:
st.sidebar.image(SideBarTop)

# Sidebar selection

# Hours or days sidebar selection(User input)
Four_Twfr = [4, 24]
hours_amt = st.sidebar.selectbox("4 or 24 Hours?", Four_Twfr)


# Number of Hours or Days sidebar selection(user input)
number_of_H_R = st.sidebar.slider("Number of H/D", min_value=1, max_value=10, value=1, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)

# Day of Rental selection(user input)
calendar_input = st.sidebar.date_input("Please select your rental date: ", value=None, min_value=None,
                                       max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)

# Time of Rental Selection(user input)
time_input = st.sidebar.time_input("Please select the time of your reservation:", value=None, key=None,
                                   help=None, on_change=None, args=None, kwargs=None, disabled=False)


#setting total amount passed

## PRICING/PRINT IF STATEMENTS WORKS ## 

if hours_amt == 4 :
    st.sidebar.write("Total Price $", Hourly * number_of_H_R)
elif hours_amt == 24 :
    st.sidebar.write("Total Price $", Daily * number_of_H_R)


#("Total Price $", Daily * number_of_H_R)
#("Total Price $", Hourly * number_of_H_R)
#st.sidebar.write(Hourly)
#st.sidebar.write(Daily)
TESTACC = '0xCb43374992d323e4F78d1954bBEa28E727a63a87'
# Rental book button!(User input)
# End of if statment also includes call to 'rent' function contained in 'Rental.sol'.
if st.sidebar.button("Book your EtherCar!!"):
    st.sidebar.write("# Succsess!")
    st.sidebar.write("Thank your for using EtherCar!!")
    st.sidebar.write("Enjoy your trip! :sunglasses:")
    st.sidebar.balloons()
    st.sidebar.image(SUCCESSimg)
    Rental = getRental()
    TESTACC.transfer(Daily * number_of_H_R)
    passPrice()
    st.sidebar.write(carId)
    st.success(Rental,SUM)
