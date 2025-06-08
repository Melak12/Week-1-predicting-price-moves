import pandas as pd
import matplotlib.pyplot as plt
from scripts.utils import get_stock_name
from textblob import TextBlob

# This script performs correlation analysis between news sentiment and stock prices.The purpose is to establish statistical correlations between the sentiment derived from news articles and the corresponding stock price movements. This involves tracking stock price changes around the date the article was published and analyzing the impact of news sentiment on stock performance. This analysis should consider the publication date and potentially the time the article was published if such data can be inferred or is available.

class CorrelationAnalyzer:
    def __init__(self, news_df, stock_df, stock_prefix):
        self.news_df = news_df
        self.stock_df = stock_df
        self.stock_prefix = stock_prefix
        self.stock_name = get_stock_name(self.stock_prefix)
    
    def convert_date_to_datetime(self):
        # Convert the 'Date' column to datetime format and normalize to date only
        self.news_df['Date'] = pd.to_datetime(self.news_df['Date'])
        self.news_df['date_only'] = self.news_df['Date'].dt.date
        self.stock_df['Date'] = pd.to_datetime(self.stock_df['Date'])
        self.stock_df['date_only'] = self.stock_df['Date'].dt.date

    def align_by_date(self):
        # Align both dataframes by date_only
        self.convert_date_to_datetime()
        # Aggregate news by date (if multiple headlines per day, average sentiment later)
        self.news_df = self.news_df.sort_values('date_only')
        self.stock_df = self.stock_df.sort_values('date_only')

    def analyze_sentiment(self, text_column='Headline'):
        # Perform sentiment analysis on news headlines
        def get_sentiment(text):
            return TextBlob(str(text)).sentiment.polarity
        self.news_df['sentiment_score'] = self.news_df[text_column].apply(get_sentiment)

    def calculate_daily_returns(self):
        # Compute daily returns for stock prices
        self.stock_df['daily_return'] = self.stock_df['Close'].pct_change()

    def merge_and_correlate(self):
        # Merge news and stock data on date_only
        # Aggregate sentiment by date (mean if multiple headlines)
        daily_sentiment = self.news_df.groupby('date_only')['sentiment_score'].mean().reset_index()
        merged = pd.merge(self.stock_df, daily_sentiment, on='date_only', how='inner')
        # Drop NA values for correlation
        merged = merged.dropna(subset=['daily_return', 'sentiment_score'])
        # Calculate correlation
        correlation = merged['daily_return'].corr(merged['sentiment_score'])
        print(f"Correlation between daily news sentiment and {self.stock_name} daily returns: {correlation:.4f}")
        return merged, correlation

    def plot_correlation(self, merged):
        # Scatter plot of sentiment vs. daily return
        plt.figure(figsize=(8, 5))
        plt.scatter(merged['sentiment_score'], merged['daily_return'], alpha=0.6)
        plt.title(f"{self.stock_name}: News Sentiment vs. Daily Stock Return")
        plt.xlabel("Daily News Sentiment Score")
        plt.ylabel("Daily Stock Return (%)")
        plt.grid(True)
        plt.show()

    def run_full_analysis(self, text_column='Headline'):
        self.align_by_date()
        self.analyze_sentiment(text_column)
        self.calculate_daily_returns()
        merged, correlation = self.merge_and_correlate()
        self.plot_correlation(merged)
        return correlation