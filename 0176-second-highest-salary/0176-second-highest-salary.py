import pandas as pd

def second_highest_salary(Employee: pd.DataFrame) -> pd.DataFrame:
    salaries = Employee["salary"].drop_duplicates().sort_values(ascending=False)
    
    if len(salaries) < 2:
        return pd.DataFrame({"SecondHighestSalary": [None]})
    
    return pd.DataFrame({"SecondHighestSalary": [salaries.iloc[1]]})
