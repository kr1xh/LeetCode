import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    counts = orders["customer_number"].value_counts()
    top_customer = counts.idxmax()
    
    return pd.DataFrame({"customer_number": [top_customer]})