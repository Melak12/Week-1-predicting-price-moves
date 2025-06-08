import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_stock_name(stock_prefix):
    # Mapping of stock prefixes to stock names
    stock_prefix_mapping = {
        "AAPL": "Apple",
        "MSFT": "Microsoft",
        "GOOGL": "Google",
        "AMZN": "Amazon",
        "TSLA": "Tesla",
        "META": "Meta",
        "NVDA": "NVIDIA",
    }
    return stock_prefix_mapping.get(stock_prefix, "Unknown Stock")

def load_financial_data(stock_prefix, base_dir="../data"):
    """Load the financial data from the base data directory."""
    filepath = f"{base_dir}/yfinance_data/{stock_prefix}_historical_data.csv"
    df = pd.read_csv(filepath)
    return df