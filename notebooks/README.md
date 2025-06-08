## Data Profiling, Cleaning & EDA Process

The following steps were performed for each stock dataset as documented in the Jupyter notebooks in the `notebooks/` directory:

### Financial News and Stock Price Integration Dataset
FNSPID (Financial News and Stock Price Integration Dataset) is a comprehensive financial dataset designed to enhance stock market predictions by combining quantitative and qualitative data.

The structure of the data is as follows:

- **headline**: Article release headline, the title of the news article, which often includes key financial actions like stocks hitting highs, price target changes, or company earnings.
- **url**: The direct link to the full news article.
- **publisher**: Author/creator of the article.
- **date**: The publication date and time, including timezone information (UTC-4 timezone).
- **stock**: Stock ticker symbol (unique series of letters assigned to a publicly traded company). For example, AAPL: Apple.

---


### Major Works in `AAPL_eda.ipynb`, `AMZN_eda.ipynb`, `GOOG_eda.ipynb`, `META_eda.ipynb`, `MSFT_eda.ipynb`, `NVDA_eda.ipynb`, and `TSLA_eda.ipynb`

For each stock dataset, the following standardized workflow was implemented:

- **Data Loading & Inspection:**
  - Loaded historical stock data using a unified utility function for each ticker (AAPL, AMZN, GOOG, META, MSFT, NVDA, TSLA).
  - Displayed the first few rows, checked the shape, and reported missing values for each dataset.

- **Datetime Handling:**
  - Converted the 'Date' column to datetime format and set it as the DataFrame index for time series analysis.

- **Stock Price Visualization:**
  - Plotted the time series of Close, Open, High, and Low prices.
  - Displayed candlestick charts for each stock using mplfinance.

- **Trend & Distribution Analysis:**
  - Analyzed and printed the frequency of up, down, and no-change trends in stock price movements.
  - Visualized the distribution of closing prices for each stock.

- **Technical Analysis Indicators:**
  - Applied TA-Lib to calculate and add:
    - 20-day and 50-day Simple Moving Averages (SMA)
    - 14-day Relative Strength Index (RSI)
    - MACD (Moving Average Convergence Divergence) and its signal/histogram
    - Daily returns, rolling volatility, cumulative returns, Bollinger Bands, and ATR
  - These indicators help analyze price trends, momentum, and volatility for further financial analysis.

- **Visualization of Technical Indicators:**
  - Visualized the close price with SMA overlays, RSI, and MACD using matplotlib for a specified date range (e.g., 2022).

---


## 🛠️ TA-Lib Installation (Windows - `.venv`)

This project uses **TA-Lib**, a library for technical analysis. Due to its native C dependencies, installation on Windows requires some extra steps.


### ✅ Step 1: Create and Activate Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate
```

### ✅ Step 2: (Optional) Register the Environment for Jupyter Notebooks

If you're working with `.ipynb` files:

```bash
pip install ipykernel
python -m ipykernel install --user --name=.venv --display-name "Python (.venv)"
```

### ✅ Step 3:  Install Project Dependencies
```bash
pip install -r requirements.txt
```


### ✅ Step 4: Install TA-Lib Binary for Windows

TA-Lib requires a compiled binary on Windows. Since it's not available as a standard `pip` install from PyPI for Windows, follow these steps:

1. Download the appropriate `.whl` (wheel) file for your Python version and system architecture from this unofficial source.

### ✅ Step 5:  Verify the Installation
```bash
import talib
print(talib.__version__)
```

---

### Correlation Analysis in `correlation_TSLA_eda.ipynb`

The notebook `correlation_TSLA_eda.ipynb` demonstrates a complete workflow for analyzing the relationship between news sentiment and TSLA stock price movements. The process leverages the `CorrelationAnalyzer` class from `scripts/correlation_analysis.py` and includes the following steps:

- **Data Loading**: Loads TSLA historical stock price data and news data (headlines, publishers, publication dates).
- **Date Alignment**: Aligns news and stock data by date, robustly handling various date formats and missing values.
- **Sentiment Analysis**: Uses TextBlob to compute sentiment polarity scores for each news headline.
- **Sentiment Aggregation**: Aggregates multiple news articles per day to compute the average daily sentiment score.
- **Stock Return Calculation**: Calculates daily percentage returns from TSLA closing prices.
- **Correlation Analysis**: Merges daily sentiment scores with daily returns and computes the Pearson correlation coefficient to assess the relationship between news sentiment and stock price movement.
- **Visualization**: Visualizes the relationship between daily sentiment and daily returns using a scatter plot.

This workflow is modular and generalizable to other stocks and news datasets by changing the stock prefix and input files. The notebook is intended for exploratory data analysis and research on the impact of news sentiment on stock price movements.

---

