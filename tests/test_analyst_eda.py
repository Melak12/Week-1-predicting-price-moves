import unittest
import pandas as pd
import numpy as np

class TestAnalystEDA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Use a small sample DataFrame for testing
        cls.df = pd.DataFrame({
            'headline': [
                'Apple stock hits new high',
                'Tesla receives price target upgrade',
                'FDA approval boosts biotech shares',
                np.nan
            ],
            'publisher': [
                'Reuters',
                'Bloomberg',
                'news@finance.com',
                'Reuters'
            ],
            'date': [
                '2021-01-01 10:00:00',
                '2021-01-02 11:00:00',
                '2021-01-03 12:00:00',
                '2021-01-04 13:00:00'
            ]
        })
        cls.df['date'] = pd.to_datetime(cls.df['date'])

    def test_headline_length(self):
        self.df['headline_length'] = self.df['headline'].str.len()
        self.assertIn('headline_length', self.df.columns)
        self.assertEqual(self.df['headline_length'].iloc[0], len('Apple stock hits new high'))

    def test_publisher_counts(self):
        counts = self.df['publisher'].value_counts()
        self.assertEqual(counts['Reuters'], 2)
        self.assertEqual(counts['Bloomberg'], 1)

    def test_date_conversion(self):
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(self.df['date']))

    def test_weekday_extraction(self):
        self.df['weekday'] = self.df['date'].dt.day_name()
        self.assertIn(self.df['weekday'].iloc[0], ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    def test_email_domain_extraction(self):
        import re
        email_pattern = re.compile(r'[\w\.-]+@[\w\.-]+\.\w+')
        email_publishers = self.df['publisher'].dropna().unique()
        email_publishers = [p for p in email_publishers if email_pattern.fullmatch(p)]
        domains = [p.split('@')[-1] for p in email_publishers]
        self.assertIn('finance.com', domains)

    def test_headline_tokenization(self):
        from nltk import word_tokenize
        from nltk.corpus import stopwords
        import nltk
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        all_headlines = ' '.join(self.df['headline'].dropna().astype(str))
        tokens = word_tokenize(all_headlines.lower())
        stop_words = set(stopwords.words('english'))
        tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
        self.assertTrue(all(isinstance(token, str) for token in tokens))
        self.assertTrue('apple' in tokens or 'tesla' in tokens)

if __name__ == '__main__':
    unittest.main()
