# Sentiment Analysis Script Documentation

The `sentiment_analysis.py` script provides a comprehensive suite of tools for analyzing the sentiment of financial news articles and their relationship to stock price movements. Below is a summary of the main features and methods implemented in this script:

## Key Features

- **Sentiment Analysis**: Implements sentiment scoring using both TextBlob and NLTK VADER. The script ensures that all required NLTK resources (including `vader_lexicon`) are available before running sentiment analysis.
- **Sentiment Classification**: Provides a `sentiment_class` method to classify articles as positive, neutral, or negative based on configurable thresholds of sentiment scores.
- **Keyword and Bigram Extraction**: Includes an optimized `identify_common_words_and_phrases` method for fast extraction and visualization of frequent keywords and bigrams in news articles.
- **Publisher Analysis**: Offers methods to analyze article frequency and sentiment by publisher, including:
  - Article frequency by weekday and month
  - Extended publication frequency analysis
  - Visualization of average sentiment and sentiment class distribution for top publishers
- **Robust Visualizations**: All visualizations are robust to missing data and missing sentiment classes, and use clear, modern plotting styles (matplotlib/seaborn).
- **Performance Optimizations**: Utilizes vectorized pandas operations and list comprehensions for efficient text and sentiment processing, suitable for large datasets.
- **Documentation and Usability**: All methods are documented with clear docstrings, and the script is structured for easy integration into notebooks and other analysis workflows.

## Notable Methods

- `__init__`: Initialize the ArticleDataAnalyzer with a DataFrame and required NLTK resources.
- `ensure_nltk_resources`: Ensure all necessary NLTK resources are available for analysis.
- `format_datetime`: Convert and extract date/time features from the 'date' column.
- `set_datetime_index`: Set the 'date' column as the DataFrame index.
- `analyze_headlines`: Compute headline length statistics and extract most common keywords and bigrams.
- `sentiment_analysis`: Perform sentiment analysis on headlines using NLTK VADER and add sentiment columns.
- `sentiment_class`: Classify sentiment scores into 'positive', 'neutral', or 'negative'.
- `analyze_articles_by_weekday`: Analyze and visualize article frequency by weekday.
- `analyze_articles_by_month`: Analyze and visualize article frequency by month.
- `extended_publication_frequency_analysis`: Highlight spikes, annotate market events, and analyze publishing times.
- `identify_common_words_and_phrases`: Efficiently extract and visualize common keywords and bigrams in headlines.
- `top_publishers_by_articles`: Analyze and visualize the number of articles per publisher.
- `common_words_by_top_publishers`: Analyze and display common words in headlines by top publishers.
- `publisher_name_analysis`: Identify publisher names that look like email addresses and extract domains.
- `visualize_sentiment_score_by_top_publishers`: Visualize average sentiment and sentiment class distribution for top publishers.

## Usage

This script is designed to be imported and used within Jupyter notebooks or other Python scripts for exploratory data analysis (EDA), technical analysis, and sentiment-driven financial research.

---

# Financial Analysis Script Documentation

The `financial_analysis.py` script provides a set of tools for performing technical and exploratory analysis on stock price data, including price visualization, technical indicator calculation, and trend analysis. Below is a summary of the main features and methods implemented in this script:

## Key Features

- **Stock Price Visualization**: Plots stock price time series (Close, Open, High, Low) and candlestick charts using matplotlib and mplfinance.
- **Technical Indicator Calculation**: Computes common technical indicators using TA-Lib, including:
  - Simple Moving Averages (SMA 20, SMA 50)
  - Relative Strength Index (RSI)
  - MACD and MACD Signal
  - Daily returns and rolling volatility
  - Cumulative returns and volatility
  - Bollinger Bands (Upper, Middle, Lower)
  - Average True Range (ATR)
- **Flexible Index Handling**: Methods to convert, set, or reset the DataFrame index to the 'Date' column for compatibility with plotting and analysis.
- **Trend Analysis**: Analyzes and prints the frequency of up, down, and no-change trends in stock price movements.
- **Distribution Visualization**: Plots the distribution of stock closing prices.
- **Correlation Placeholder**: Includes a placeholder for future sentiment/price correlation analysis.

## Notable Methods

- `__init__`: Initialize the FinancialDataAnalyzer with a DataFrame and stock prefix.
- `get_stock_name`: Map stock prefix to full stock name.
- `change_to_datetime`: Convert the 'Date' column to datetime and set as index.
- `set_date_as_index`: Set the 'Date' column as the DataFrame index.
- `reset_index`: Reset the DataFrame index to columns.
- `plot_stock_prices`: Plot time series of stock prices and candlestick chart.
- `calculate_technical_indicators`: Compute SMA, RSI, MACD, returns, volatility, Bollinger Bands, and ATR.
- `plot_technical_indicators`: Visualize technical indicators over a specified date range.
- `analyze_stock_price_trends`: Analyze and print the frequency of price trends (up, down, no change).
- `visualize_stock_price_distribution`: Plot the distribution of closing prices.
- `correlate_sentiment_with_stock_prices`: Placeholder for sentiment/price correlation analysis.

## Usage

This script is designed to be imported and used within Jupyter notebooks or other Python scripts for financial EDA, technical analysis, and stock price research. See the EDA notebooks for example usage and integration with other analysis workflows.

---

# Correlation Analysis Script Documentation

The `correlation_analysis.py` script provides tools for analyzing the relationship between news sentiment and stock price movements. It is designed to align news and stock data by date, perform sentiment analysis on news headlines, compute daily stock returns, and statistically test the correlation between sentiment and returns.

## Key Features

- **Date Alignment**: Robustly aligns news and stock data by date, handling various date formats and missing values.
- **Sentiment Analysis**: Uses TextBlob to compute sentiment polarity scores for news headlines, with support for custom headline columns.
- **Sentiment Aggregation**: Aggregates multiple news articles per day to compute average daily sentiment scores.
- **Stock Return Calculation**: Computes daily percentage returns from closing prices.
- **Correlation Analysis**: Calculates the Pearson correlation coefficient between average daily sentiment and daily stock returns, providing statistical insight into their relationship.
- **Visualization**: Includes scatter plot visualization of sentiment scores versus daily returns.
- **Flexible Integration**: Designed for use in Jupyter notebooks and Python scripts, with a workflow that can be run step-by-step or as a full analysis pipeline.

## Notable Methods

- `__init__`: Initialize the CorrelationAnalyzer with news and stock DataFrames and a stock prefix.
- `convert_date_to_datetime`: Robustly convert and normalize date columns in both DataFrames, handling mixed formats and missing values.
- `align_by_date`: Align and sort both DataFrames by date, preparing them for analysis.
- `analyze_sentiment`: Compute sentiment polarity scores for news headlines using TextBlob.
- `calculate_daily_returns`: Compute daily percentage returns for stock closing prices.
- `merge_and_correlate`: Aggregate daily sentiment, merge with stock returns, and compute the Pearson correlation coefficient.
- `plot_correlation`: Visualize the relationship between sentiment and returns with a scatter plot.
- `run_full_analysis`: Run the entire workflow from alignment to correlation and visualization.

## Usage

This script is intended for exploratory data analysis (EDA) and research on the impact of news sentiment on stock price movements. It is suitable for use in Jupyter notebooks and can be integrated with other analysis scripts. See the EDA notebooks for example usage and workflow integration.

---
