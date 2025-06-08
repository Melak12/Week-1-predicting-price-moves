import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_financial_data(stock_prefix, base_dir="../data"):
    """Load the financial data from the base data directory."""
    filepath = f"{base_dir}/yfinance_data/{stock_prefix}_historical_data.csv"
    df = pd.read_csv(filepath)
    return df