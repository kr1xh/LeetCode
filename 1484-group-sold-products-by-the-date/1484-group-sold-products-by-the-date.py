import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    result = (
        activities
        .groupby("sell_date")["product"]
        .apply(lambda x: sorted(x.unique()))
        .reset_index()
    )
    
    result["num_sold"] = result["product"].apply(len)
    result["products"] = result["product"].apply(lambda x: ",".join(x))
    
    return result[["sell_date", "num_sold", "products"]] \
        .sort_values("sell_date")