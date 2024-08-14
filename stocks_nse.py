#from urllib import response
import streamlit as st
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
st.header('Indian Stock Dashboard')

ticker = st.sidebar.text_input('Symbol Code','INFY')
exchange = st.sidebar.text_input('Exchnge','NSE') #NSE , BSE
url = f'https://www.google.com/finance/quote/{ticker}:{exchange}'   


#for i in range(3):
response = requests.get(url)
soup= BeautifulSoup(response.text,'html.parser')
#class1 = "YMlKec fxKbKc"

price = float(soup.find(class_="YMlKec fxKbKc").text.strip()[1:].replace(",", ""))
previous_close= float(soup.find(class_="P6K39c").text.strip()[1:].replace(",", ""))
#day_range = float(soup.find(class_="P6K39c").text.strip()[1:].replace(",", ""))

revenue = soup.find(class_="QXDnM").text   #str(soup.find(class_="P6K39c").text)
news = soup.find(class_ = "Yfwt5").text
#print(price)
    #time.sleep(10)
about = soup.find(class_ = "bLLb2d").text
fount= soup.find(class_ = "EY8ABd-OWXEXe-TAWMXe").text.strip()[1:].replace(",", "")
#pe = soup.find(class_  ="gyFHrc")
dict1 = {'Price':price,
        'Previous Close Price':previous_close,
        'Revenue':revenue,
        'Fount':fount,
        'News':news,
        'About':about}
df = pd.DataFrame(dict1,index =[ 'Extracted Data']).T

st.write(df)  
#r= soup.find(class_="QXDnM").text   
#st.write('Curren tPrice:',price)
#st.write('Previous Close Price:',previous_close)
#st.write('Day range:',day_range)
#st.write("The Revenue is : ",revenue)
#st.write(r)
#st.write('News',news)
#st.write('About information of Stcoks:',about)

