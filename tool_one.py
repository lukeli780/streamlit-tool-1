import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
from datetime import date

st.title('Stock Price Change Plot')

ticker = st.text_input("Tickers")
s_date = st.date_input("start date", date(2019, 1, 1))
e_date = st.date_input("end date")
intvl = st.select_slider("interval", options=['1d', '5d', '1wk', '1mo', '3mo'])

if len(ticker) != 0:
    stock = yf.download(ticker, start=s_date, end=e_date, interval=intvl)
    # stock=pd.DataFrame(stock)
    stock = stock['Adj Close']
    stock[:] = ((stock[:] / stock.iloc[0] - 1) * 100)
    stock

    st.line_chart(stock)
else:
    st.write("please enter the ticker")


