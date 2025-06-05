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