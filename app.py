import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Streamlit title and description
st.title("Stock Price Visualization")
st.markdown("""
This app allows you to visualize the stock prices of any company over a selected time period.
Use the inputs below to choose the stock and date range.
""")

# Stock ticker input
ticker = st.text_input("Enter stock ticker (e.g. AAPL, MSFT, TSLA):", "AAPL")

# Date range input
start_date = st.date_input("Start date", pd.to_datetime("2023-01-01"))
end_date = st.date_input("End date", pd.to_datetime("2024-01-01"))

# Fetch stock data based on user input
if ticker:
    try:
        # Download stock data
        stock_data = yf.download(ticker, start=start_date, end=end_date)

        # Check if the data is empty
        if stock_data.empty:
            st.error(f"No data found for {ticker}. Please check the ticker symbol and try again.")
        else:
            # Display larger text using markdown and HTML for better visibility
            st.markdown(f"### Showing stock data for **{ticker}** from **{start_date}** to **{end_date}**", unsafe_allow_html=True)

            # Display the stock data with a larger font size using st.dataframe
            st.dataframe(stock_data, use_container_width=True)  # This shows the data in a nice table format

            # Plotting the closing prices
            st.subheader(f"{ticker} Closing Price")
            
            # Create the figure and axis
            plt.figure(figsize=(10,6))  # Adjust the figure size
            plt.plot(stock_data['Close'], label=f'{ticker} Closing Price', color='blue')
            
            # Add title and labels
            plt.title(f'{ticker} Stock Prices from {start_date} to {end_date}')
            plt.xlabel('Date')
            plt.ylabel('Price (USD)')
            plt.legend(loc='upper left')
            plt.grid(True)

            # Improve x-axis readability by rotating the dates
            plt.xticks(rotation=45)

            # Display the plot using Streamlit's pyplot function
            st.pyplot(plt)  # This replaces plt.show()

    except Exception as e:
        st.error(f"Error fetching data for {ticker}. Please try again.")
        st.exception(e)
