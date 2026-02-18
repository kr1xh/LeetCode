import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    distinct_salaries = (
        employee["salary"]
        .drop_duplicates()
        .sort_values(ascending=False)
        .reset_index(drop=True)
    )
    
    if len(distinct_salaries) >= 2:
        result = distinct_salaries.iloc[1]
    else:
        result = None
    
    return pd.DataFrame(
        {"SecondHighestSalary": [result]}
    )