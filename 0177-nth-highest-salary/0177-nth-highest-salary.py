import pandas as pd

def nth_highest_salary(Employee: pd.DataFrame, n: int) -> pd.DataFrame:
    col_name = f"getNthHighestSalary({n})"
    
    if n <= 0:
        return pd.DataFrame({col_name: [None]})
    
    salaries = Employee["salary"].drop_duplicates().sort_values(ascending=False)
    
    if len(salaries) < n:
        return pd.DataFrame({col_name: [None]})
    
    return pd.DataFrame({col_name: [salaries.iloc[n - 1]]})
