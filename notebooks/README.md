## Data Profiling, Cleaning & EDA Process

The following steps were performed for each country dataset as documented in the Jupyter notebooks in the `notebooks/` directory:

### Financial News and Stock Price Integration Dataset
FNSPID (Financial News and Stock Price Integration Dataset), is a comprehensive financial dataset designed to enhance stock market predictions by combining quantitative and qualitative data.

The structure of the data is as follows:

- **headline**: Article release headline, the title of the news article, which often includes key financial actions like stocks hitting highs, price target changes, or company earnings.
- **url**: The direct link to the full news article.
- **publisher**: Author/creator of the article.
- **date**: The publication date and time, including timezone information (UTC-4 timezone).
- **stock**: Stock ticker symbol (unique series of letters assigned to a publicly traded company). For example, AAPL: Apple.

---

### Major Works in `analyst_eda.ipynb`

- **Headline Length Analysis:** Computed descriptive statistics for headline lengths.
- **Publisher Analysis:** Counted articles per publisher, identified top publishers, and analyzed common keywords for each.
- **Publication Date Analysis:** Converted date columns, extracted day and weekday, and visualized article publication trends over time and by weekday.
- **Keyword and Phrase Extraction:** Used NLP techniques to identify the most common keywords and bigrams in headlines.
- **Time Series Analysis:** Highlighted spikes in publication frequency and annotated major market events.
- **Hourly Publication Analysis:** Analyzed distribution of article publications by hour of day (if time data available).
- **Publisher Email Domain Extraction:** Identified publisher names formatted as email addresses and summarized top domains.

---

### Major Works in `TSLA_eda.ipynb`

- **Summary Statistics & Missing Value Report:** Loaded TSLA historical data, displayed summary statistics for numeric columns, reported missing values, and listed columns with >5% nulls.
- **Technical Analysis Indicators:** Applied TA-Lib to calculate and add:
  - 20-day and 50-day Simple Moving Averages (SMA)
  - 14-day Relative Strength Index (RSI)
  - MACD (Moving Average Convergence Divergence) and its signal/histogram
  These indicators help analyze TSLA price trends and momentum for further financial analysis.
- **Visualization of Technical Indicators:** Visualized the TSLA close price with SMA overlays, RSI, and MACD using matplotlib to better understand the impact of these indicators on stock price trends.

---

### Major Works in `AAPL_eda.ipynb`, `AMZN_eda.ipynb`, `GOOG_eda.ipynb`, `META_eda.ipynb`, `MSFT_eda.ipynb`, `NVDA_eda.ipynb`, and `TSLA_eda.ipynb`

For each stock dataset:

- **Summary Statistics & Missing Value Report:** Loaded historical data, displayed summary statistics for numeric columns, reported missing values, and listed columns with >5% nulls.
- **Technical Analysis Indicators:** Applied TA-Lib to calculate and add:
  - 20-day and 50-day Simple Moving Averages (SMA)
  - 14-day Relative Strength Index (RSI)
  - MACD (Moving Average Convergence Divergence) and its signal/histogram
  These indicators help analyze price trends and momentum for further financial analysis.
- **Visualization of Technical Indicators:** Visualized the close price with SMA overlays, RSI, and MACD using matplotlib to better understand the impact of these indicators on stock price trends.

---

### Major Works in `comparison.ipynb`

- **Date Alignment:** Loaded and aligned news and stock price data by date, normalizing timestamps for accurate comparison.
- **Sentiment Analysis:** Used TextBlob to quantify the sentiment (positive, negative, neutral) of news headlines, and aggregated daily sentiment scores.
- **Daily Stock Returns:** Computed daily percentage changes in closing prices to represent stock movements.
- **Correlation Analysis:** Merged daily sentiment and stock returns, calculated the correlation coefficient, and visualized the correlation using a heatmap.
- **Visualization:** Plotted daily sentiment and stock returns over time to visually assess their relationship.

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

1. Download the appropriate `.whl` (wheel) file for your Python version and system architecture from this unofficial sour

### ✅ Step 5:  Verify the Installation
```bash
import talib
print(talib.__version__)
```

