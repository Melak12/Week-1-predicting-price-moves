import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(filename, base_dir="../data"):
    """Load CSV data from the base data directory."""
    filepath = f"{base_dir}/{filename}"
    df = pd.read_csv(filepath)
    return df