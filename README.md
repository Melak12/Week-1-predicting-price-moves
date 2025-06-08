# Week 1 - Predicting Price Moves with News Sentiment
This project focuses on the detailed analysis of a large corpus of financial news data to discover correlations between news sentiment and stock market movements. This challenge is designed to refine your skills in Data Engineering (DE), Financial Analytics (FA), and Machine Learning Engineering (MLE).

### Business Objective
Nova Financial Solutions aims to enhance its predictive analytics capabilities to significantly boost its financial forecasting accuracy and operational efficiency through advanced data analysis. As a Data Analyst at Nova Financial Solutions,  your primary task is to conduct a rigorous analysis of the financial news dataset. The focus of your analysis should be two-fold:

Sentiment Analysis: Perform sentiment analysis on the ‘headline’ text to quantify the tone and sentiment expressed in financial news. This will involve using natural language processing (NLP) techniques to derive sentiment scores, which can be associated with the respective 'Stock Symbol' to understand the emotional context surrounding stock-related news.
Correlation Analysis: Establish statistical correlations between the sentiment derived from news articles and the corresponding stock price movements. This involves tracking stock price changes around the date the article was published and analyzing the impact of news sentiment on stock performance. This analysis should consider the publication date and potentially the time the article was published if such data can be inferred or is available.

### Datashet Overview
FNSPID (Financial News and Stock Price Integration Dataset), is a comprehensive financial dataset designed to enhance stock market predictions by combining quantitative and qualitative data.

The structure of the [data](https://drive.google.com/drive/folders/1rsispvTGPjC8pbKS-yYb-6dcJiXTKSAv?usp=drive_link) is as follows

headline: Article release headline, the title of the news article, which often includes key financial actions like stocks hitting highs, price target changes, or company earnings.
url: The direct link to the full news article.
publisher: Author/creator of article.
date: The publication date and time, including timezone information(UTC-4 timezone).
stock: Stock ticker symbol (unique series of letters assigned to a publicly traded company). For example (AAPL: Apple)

## Setup
1. Clone: `git clone https://github.com/Melak12/Week-1-predicting-price-moves.git`
2. Create venv: `python3 -m venv .venv`
3. Activate: `source .venv/bin/activate` (macOS/Linux) or `.venv\Scripts\activate` (Windows)
4. Install: `pip install -r requirements.txt`

Note: if requirements.txt is missing, you might need to run this command
`pip freeze > requirements.txt`

## Project Structure

The repository is organized as follows:

```
README.md
requirements.txt
app/
    __init__.py

data/
    raw_analyst_ratings.csv
    yfinance_data/
        AAPL_historical_data.csv
        AMZN_historical_data.csv
        GOOG_historical_data.csv
        META_historical_data.csv
        MSFT_historical_data.csv
        NVDA_historical_data.csv
        TSLA_historical_data.csv
notebooks/
    __init__.py
    AAPL_eda.ipynb
    AMZN_eda.ipynb
    comparison.ipynb
    GOOG_eda.ipynb
    META_eda.ipynb
    MSFT_eda.ipynb
    news_sentiment_eda.ipynb
    NVDA_eda.ipynb
    README.md
    TSLA_eda.ipynb
scripts/
    __init__.py
    financial_analysis.py
    README.md
    sentiment_analysis.py
    utils.py
tests/
    __init__.py
    test_analyst_eda.py
```

## Notebooks Overview

The `notebooks/` directory contains detailed exploratory data analysis (EDA) and correlation analysis for both news and stock price data:

- **news_sentiment_eda.ipynb**: EDA on news headlines, including headline length, publisher analysis, keyword extraction, time series analysis, and email domain extraction.
- **TSLA_eda.ipynb, AAPL_eda.ipynb, AMZN_eda.ipynb, GOOG_eda.ipynb, META_eda.ipynb, MSFT_eda.ipynb, NVDA_eda.ipynb**: For each stock, these notebooks load historical price data, report summary statistics and missing values, compute technical indicators (SMA, RSI, MACD) using TA-Lib, and visualize the results.
- **comparison.ipynb**: Aligns news and stock data by date, performs sentiment analysis on headlines, calculates daily stock returns, and analyzes the correlation between news sentiment and stock price movements. Includes both time series and heatmap visualizations of the correlation.

See the `notebooks/README.md` for more details on each notebook's workflow and outputs.