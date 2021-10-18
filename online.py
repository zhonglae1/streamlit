import streamlit as st
import yfinance as yf
import pandas as pd
import datetime as dt
st.markdown('''
# Stonks
***
''')

st.sidebar.subheader("Input parameters here:")
start_date = st.sidebar.date_input("Start date", dt.date(2015, 1, 1))
end_date = st.sidebar.date_input("End date", dt.date(2020, 1, 1))

ticker_list = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list) # Select ticker symbol
tickerData = yf.Ticker(tickerSymbol) # Get ticker data
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)['Close']

print(tickerDf)
st.line_chart(tickerDf)