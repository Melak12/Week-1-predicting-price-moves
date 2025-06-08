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

For more details, see the docstrings within `sentiment_analysis.py` and the example usage in the EDA notebooks.
