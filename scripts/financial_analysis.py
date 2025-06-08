import pandas as pd
import matplotlib.pyplot as plt
import talib
import mplfinance as mpf
from scripts.utils import get_stock_name

## This script performs financial analysis based on the data provided in a DataFrame which is loaded from ../data/yfinance_data/<STOCKPREFIX>_historical_data.csv. Here is the mapping of the STOCKPREFIX to the stock name:
# STOCKPREFIX = {
#     "AAPL": "Apple",
#     "MSFT": "Microsoft",
#     "GOOGL": "Google",
#     "AMZN": "Amazon",
#     "TSLA": "Tesla",
#     "META": "Meta",
#     "NVDA": "NVIDIA",
# }

class FinancialDataAnalyzer:
    def __init__(self, df, stock_prefix):
        self.df = df
        self.stock_prefix = stock_prefix
        self.stock_name = get_stock_name(self.stock_prefix)

    def change_to_datetime(self):
        # Convert the 'Date' column to datetime format
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df.set_index('Date', inplace=True)

    def set_date_as_index(self):
        # Ensure the 'Date' column is set as the index
        if 'Date' in self.df.columns:
            self.df.set_index('Date', inplace=True)
        else:
            raise ValueError("The DataFrame does not contain a 'Date' column.")
    def reset_index(self):
        # Reset the index of the DataFrame
        self.df.reset_index(['Date'], inplace=True)

    def plot_stock_prices(self):
        # Plot the stock prices over time and candlestick chart
        plt.figure(figsize=(14, 7))
        plt.plot(self.df.index, self.df['Close'], label='Close Price', color='blue', alpha=0.1)
        plt.plot(self.df.index, self.df['Open'], label='Open Price', color='orange', alpha=0.5) # Plotting Open Price
        plt.plot(self.df.index, self.df['High'], label='High Price', color='green', alpha=0.7) # Plotting High Price
        plt.plot(self.df.index, self.df['Low'], label='Low Price', color='red', alpha=0.6) # Plotting Low Price
        plt.title(f'{self.stock_name} Stock Prices Over Time')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid()
        plt.show()

        # self.set_date_as_index()
        mpf.plot(self.df, type='candle', style='charles',
                 title=f'{self.stock_name} Stock Prices',
                 ylabel='Price (USD)', volume=True)
    
    def calculate_technical_indicators(self):
        # Calculate technical indicators using TA-Lib
        self.df['SMA_20'] = talib.SMA(self.df['Close'], timeperiod=20)
        self.df['SMA_50'] = talib.SMA(self.df['Close'], timeperiod=50)
        self.df['RSI'] = talib.RSI(self.df['Close'], timeperiod=14)
        self.df['MACD'], self.df['MACD_signal'], _ = talib.MACD(self.df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
        self.df['Return'] = self.df['Close'].pct_change()  # Daily returns
        self.df['Volatility'] = self.df['Return'].rolling(window=20).std()
        self.df['cumulative_return'] = (1 + self.df['Return']).cumprod() - 1  # Cumulative returns
        self.df['cumulative_volatility'] = (1 + self.df['Volatility']).cumprod() - 1
        self.df['Upper_BB'], self.df['Middle_BB'], self.df['Lower_BB'] = talib.BBANDS(self.df['Close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
        self.df['ATR'] = talib.ATR(self.df['High'], self.df['Low'], self.df['Close'], timeperiod=14)

    def plot_technical_indicators(self, start_date, end_date):
        # Plot technical indicators over a specified date range
        filtered_df = self.df[(self.df.index >= start_date) & (self.df.index <= end_date)]
        
        plt.figure(figsize=(14, 10))
        
        # Plot Close Price and SMA
        plt.subplot(3, 1, 1)
        plt.plot(filtered_df.index, filtered_df['Close'], label='Close Price', color='blue')
        plt.plot(filtered_df.index, filtered_df['SMA_20'], label='20-Day SMA', color='orange')
        plt.plot(filtered_df.index, filtered_df['SMA_50'], label='50-Day SMA', color='green')
        plt.title(f'{self.stock_name} Stock Price and Technical Indicators')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid()

        # Plot RSI
        plt.subplot(3, 1, 2)
        plt.plot(filtered_df.index, filtered_df['RSI'], label='RSI', color='purple')
        plt.axhline(70, linestyle='--', alpha=0.5, color='red')
        plt.axhline(30, linestyle='--', alpha=0.5, color='green')
        plt.title('Relative Strength Index (RSI)')
        plt.xlabel('Date')
        plt.ylabel('RSI Value')
        plt.legend()
        plt.grid()

        # Plot MACD
        plt.subplot(3, 1, 3)
        plt.plot(filtered_df.index, filtered_df['MACD'], label='MACD', color='blue')
        plt.plot(filtered_df.index, filtered_df['MACD_signal'], label='MACD Signal', color='orange')
        plt.title('Moving Average Convergence Divergence (MACD)')
        plt.xlabel('Date')
        plt.ylabel('MACD Value')
        plt.legend()
        plt.grid()

        plt.tight_layout()
        plt.show()  

    def analyze_stock_price_trends(self):
        # Analyze stock price trends
        self.df['Trend'] = self.df['Close'].diff().apply(lambda x: 'Up' if x > 0 else 'Down' if x < 0 else 'No Change')
        trend_counts = self.df['Trend'].value_counts()
        print(f"Stock Price Trend Analysis for {self.stock_name}:\n{trend_counts}")

    def visualize_stock_price_distribution(self):
        # Visualize the distribution of stock prices
        plt.figure(figsize=(10, 6))
        plt.hist(self.df['Close'], bins=50, color='blue', alpha=0.7)
        plt.title(f'{self.stock_name} Stock Price Distribution')
        plt.xlabel('Price (USD)')
        plt.ylabel('Frequency')
        plt.grid()
        plt.show()

    def correlate_sentiment_with_stock_prices(self):
        # Placeholder for sentiment analysis correlation
        # This function would require sentiment data to be merged with stock prices
        print("Sentiment analysis correlation is not implemented yet.")
        # Example: self.df['Sentiment'] = sentiment_data['Sentiment']
        # self.df['Sentiment_Correlation'] = self.df['Close'].corr(self.df['Sentiment'])
