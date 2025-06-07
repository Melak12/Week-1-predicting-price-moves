import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize, ngrams, FreqDist
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
from collections import Counter


# Download NLTK resources if not already present
print("Downloading NLTK resources...")
nltk.download('punkt', quiet=True, force=True)
nltk.download('punkt_tab', quiet=True, force=True)
nltk.download('stopwords', quiet=True, force=True)
nltk.download('wordnet', quiet=True, force=True)
nltk.download('vader_lexicon', quiet=True, force=True)
print("NLTK resources downloaded.")

class ArticleDataAnalyzer:
    def __init__(self, df):
        # Initialize the ArticleDataAnalyzer with a DataFrame
        self.df = df
        self.ensure_nltk_resources()
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = nltk.WordNetLemmatizer()

    def ensure_nltk_resources(self):
        # Ensure NLTK resources are available
        try:
            nltk.data.find('tokenizers/punkt')
            nltk.data.find('corpora/stopwords')
            nltk.data.find('corpora/wordnet')
            nltk.data.find('sentiment/vader_lexicon.zip')
            print("NLTK resources are available.")
        except LookupError:
            print("NLTK resources not found. Downloading...")
            nltk.download('punkt', quiet=True)
            nltk.download('stopwords', quiet=True)
            nltk.download('wordnet', quiet=True)
            nltk.download('vader_lexicon', quiet=True)
            print("NLTK resources downloaded.")

    def format_datetime(self):
        # Convert 'date' column to datetime format
        if 'date' in self.df.columns:
            self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce', utc=True)
            self.df['year'] = self.df['date'].dt.year
            self.df['month'] = self.df['date'].dt.month
            self.df['day'] = self.df['date'].dt.day
            self.df['hour'] = self.df['date'].dt.hour
            self.df['minute'] = self.df['date'].dt.minute
            self.df['dayOfWeek'] = self.df['date'].dt.dayofweek
            self.df['date_only'] = self.df['date'].dt.date
            self.df['weekday'] = self.df['date'].dt.day_name()
            print("Date column formatted to datetime.")
        else:
            print("No 'date' column found in DataFrame.")

    def set_datetime_index(self):
        # Set 'date' as the DataFrame index if not already set
        if self.df.index.name != 'date':
            self.df.set_index('date', inplace=True)
            print("Date column set as index.")
        else:
            print("Date column is already set as index.")

    def analyze_headlines(self):
        # Combine all headlines into a single text
        all_headlines = ' '.join(self.df['headline'].dropna().astype(str))

        # Calculate headline length statistics
        self.df['headline_length'] = self.df['headline'].str.len()
        headline_stats = self.df['headline_length'].describe()
        print(headline_stats)

        # Tokenize and clean
        tokens = word_tokenize(all_headlines.lower())
        stop_words = set(stopwords.words('english'))
        tokens = [word for word in tokens if word.isalpha() and word not in stop_words]

        # Get most common keywords (unigrams)
        fdist = FreqDist(tokens)
        print("Most common keywords:")
        print(fdist.most_common(20))

        # Get most common bigrams (phrases)
        bigrams = ngrams(tokens, 2)
        bigram_fdist = FreqDist(bigrams)
        print("\nMost common bigrams (phrases):")
        for phrase, count in bigram_fdist.most_common(20):
            print(' '.join(phrase), ":", count)
    
    def analyze_sentiment(self):
        # Ensure VADER sentiment analyzer is available
        from nltk.sentiment import SentimentIntensityAnalyzer
        sia = SentimentIntensityAnalyzer()

        # Analyze sentiment of each headline
        self.df['sentiment'] = self.df['headline'].apply(lambda x: sia.polarity_scores(str(x)) if pd.notnull(x) else None)

        # Extract compound score for overall sentiment
        self.df['compound'] = self.df['sentiment'].apply(lambda x: x['compound'] if x else None)

        print("Sentiment analysis completed. Compound scores added to DataFrame.")

    def analyze_articles_by_weekday(self):
        # Count and visualize articles published by weekday
        if 'dayOfWeek' in self.df.columns and 'weekday' in self.df.columns:
            # Group by weekday name for correct order
            weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            articles_per_day = self.df['weekday'].value_counts().reindex(weekday_order, fill_value=0)
            print("Articles published by weekday:")
            print(articles_per_day)

            # Plotting
            plt.figure(figsize=(12, 6))
            articles_per_day.plot(kind='bar')
            plt.title('Articles Published by Weekday')
            plt.xlabel('Weekday')
            plt.ylabel('Number of Articles')
            plt.xticks(rotation=45)
            plt.show()
        else:
            print("'dayOfWeek' or 'weekday' column not found in DataFrame.")
    
    def analyze_articles_by_month(self):
        # Count and visualize articles published by month
        if 'month' in self.df.columns:
            # Map month numbers to month names
            month_order = [
                'January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December'
            ]
            def safe_month_name(x):
                try:
                    if pd.notnull(x) and int(x) == x and 1 <= int(x) <= 12:
                        return month_order[int(x)-1]
                except Exception:
                    pass
                return 'Unknown'
            self.df['month_name'] = self.df['month'].apply(safe_month_name)
            articles_per_month = self.df['month_name'].value_counts().reindex(month_order, fill_value=0)
            print("Articles published by month:")
            print(articles_per_month)

            # Plotting
            plt.figure(figsize=(12, 6))
            articles_per_month.plot(kind='bar')
            plt.title('Articles Published by Month')
            plt.xlabel('Month')
            plt.ylabel('Number of Articles')
            plt.xticks(rotation=45)
            plt.show()
        else:
            print("'month' column not found in DataFrame.")
    
    def extended_publication_frequency_analysis(self):
        # Let's enhance the analysis by:
        # 1. Highlighting spikes (outliers) in publication frequency
        # 2. Annotating known market events (example: COVID-19 crash, etc.)
        # 3. Analyzing publishing times (hour of day) if time data is available


        # 1. Highlight spikes in publication frequency
        if 'date' in self.df.columns:
            articles_per_day = self.df.groupby(self.df['date'].dt.date).size()
            mean_count = articles_per_day.mean()
            std_count = articles_per_day.std()
            spike_threshold = mean_count + 3 * std_count
            spikes = articles_per_day[articles_per_day > spike_threshold]

            plt.figure(figsize=(14, 5))
            articles_per_day.plot(label='Articles per Day')
            plt.scatter(spikes.index, spikes.values, color='red', label='Spikes (>3σ)', zorder=5)
            plt.title('Number of Articles Published Per Day with Spikes Highlighted')
            plt.xlabel('Date')
            plt.ylabel('Article Count')
            plt.legend()
            plt.tight_layout()
            plt.show()

            # 2. Annotate known market events (example: COVID-19 crash)
            # You can add more events as needed
            event_dates = {
                'COVID-19 Crash': '2020-03-16',
                '2016 Election': '2016-11-08',
                'Brexit Vote': '2016-06-23'
            }
            plt.figure(figsize=(14, 5))
            articles_per_day.plot(label='Articles per Day')
            for event, date in event_dates.items():
                if date in articles_per_day.index.astype(str):
                    plt.axvline(date, color='orange', linestyle='--', alpha=0.7)
                    plt.text(date, plt.ylim()[1]*0.95, event, rotation=90, verticalalignment='top', color='orange')
            plt.title('Articles Published Per Day with Major Market Events')
            plt.xlabel('Date')
            plt.ylabel('Article Count')
            plt.tight_layout()
            plt.show()

            # 3. Analyze publishing times (hour of day)
            if 'date' in self.df.columns and pd.api.types.is_datetime64_any_dtype(self.df['date']):
                self.df['hour'] = self.df['date'].dt.hour
                hour_counts = self.df['hour'].value_counts().sort_index()
                plt.figure(figsize=(10, 4))
                hour_counts.plot(kind='bar')
                plt.title('Distribution of Article Publications by Hour of Day')
                plt.xlabel('Hour of Day')
                plt.ylabel('Article Count')
                plt.tight_layout()
                plt.show()
            else:
                print("No time information available in 'date' column for hourly analysis.")

            # Summary:
            # - Spikes in publication frequency are highlighted.
            # - Major market events are annotated.
            # - Publishing time distribution is shown if time data is available.
                # Publisher Analysis
        else:
            print("No 'date' column or datetime index found for publication frequency analysis.")
            return
    
    def identify_common_words_and_phrases(self, top_n=20):
        # Efficiently identify and visualize common keywords and bigrams in headlines
        # Use pandas vectorized string operations for faster processing
        headlines = self.df['headline'].dropna().astype(str).str.lower()
        # Tokenize all headlines at once using pandas explode
        tokens = headlines.str.split().explode()
        # Remove stopwords and non-alpha tokens efficiently
        stop_words = self.stop_words
        tokens = tokens[tokens.str.isalpha() & ~tokens.isin(stop_words)]
        # Get most common keywords (unigrams)
        fdist = tokens.value_counts().head(top_n)
        print("Most common keywords:")
        print(fdist)
        # Visualize unigrams
        plt.figure(figsize=(10, 5))
        sns.barplot(x=fdist.values, y=fdist.index, palette='Blues_d')
        plt.title(f'Top {top_n} Most Common Keywords in Headlines')
        plt.xlabel('Frequency')
        plt.ylabel('Keyword')
        plt.tight_layout()
        plt.show()
        # For bigrams, use pandas rolling window for efficiency
        
        bigrams = headlines.apply(lambda x: [tuple(x.split()[i:i+2]) for i in range(len(x.split())-1)])
        bigram_list = [bigram for sublist in bigrams for bigram in sublist if all(word.isalpha() and word not in stop_words for word in bigram)]
        bigram_counts = Counter(bigram_list).most_common(top_n)
        print(f"\nMost common bigrams (phrases):")
        for phrase, count in bigram_counts:
            print(' '.join(phrase), ":", count)
        # Visualize bigrams
        if bigram_counts:
            phrases, counts = zip(*bigram_counts)
            phrases = [' '.join(p) for p in phrases]
            plt.figure(figsize=(10, 5))
            sns.barplot(x=list(counts), y=list(phrases), palette='Greens_d')
            plt.title(f'Top {top_n} Most Common Bigrams in Headlines')
            plt.xlabel('Frequency')
            plt.ylabel('Bigram Phrase')
            plt.tight_layout()
            plt.show()
       

    def top_publishers_by_articles(self):
        # Analyze and visualize the number of articles per publisher
        # Count articles per publisher
        if 'publisher' in self.df.columns:
            publisher_counts = self.df['publisher'].value_counts()
            top_publishers = publisher_counts.head(30)

            # Plotting
            plt.figure(figsize=(12, 6))
            sns.barplot(x=top_publishers.index, y=top_publishers.values, palette='viridis')
            plt.title('Top 30 Publishers by Number of Articles')
            plt.xlabel('Publisher')
            plt.ylabel('Number of Articles')
            plt.xticks(rotation=90)
            plt.show()

        else:
            print("No 'publisher' column found in DataFrame.")
    
    def common_words_by_top_publishers(self):
        # Analyze and visualize common words in headlines by top publishers
        if 'publisher' in self.df.columns and 'headline' in self.df.columns:
            top_publishers = self.df['publisher'].value_counts().head(30).index
            top_publisher_df = self.df[self.df['publisher'].isin(top_publishers)]

            # Combine all headlines for each publisher
            publisher_headlines = top_publisher_df.groupby('publisher')['headline'].apply(lambda x: ' '.join(x.dropna()))

            # Tokenize and clean
            tokens = publisher_headlines.apply(lambda x: word_tokenize(x.lower()))
            tokens = tokens.apply(lambda x: [word for word in x if word.isalpha() and word not in self.stop_words])

            # Get most common words for each publisher
            common_words = tokens.apply(lambda x: FreqDist(x).most_common(20))

            print("\nMost common words by top publishers:")
            for publisher, words in common_words.items():
                print(f"\n{publisher}:")
                for word, count in words:
                    print(f"{word}: {count}")

        else:
            print("No 'publisher' or 'headline' column found in DataFrame.")

    def publisher_name_analysis(self):
        #Identify publisher names that look like email addresses and extract domains
        # Regex for email addresses
        email_pattern = re.compile(r'[\w\.-]+@[\w\.-]+\.\w+')
        email_publishers = self.df['publisher'].dropna().unique()
        email_publishers = [p for p in email_publishers if email_pattern.fullmatch(p)]

        # Extract domains
        domains = [p.split('@')[-1] for p in email_publishers]
        domain_counts = pd.Series(domains).value_counts()
        print("\nTop email domains among publishers:")
        print(domain_counts.head(10))