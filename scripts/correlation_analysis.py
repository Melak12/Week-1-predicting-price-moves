import pandas as pd
import matplotlib.pyplot as plt
from scripts.utils import get_stock_name

class CorrelationAnalyzer:
    def __init__(self, news_df, stock_df, stock_prefix):
        self.news_df = news_df
        self.stock_df = stock_df
        self.stock_prefix = stock_prefix
        self.stock_name = get_stock_name(self.stock_prefix)