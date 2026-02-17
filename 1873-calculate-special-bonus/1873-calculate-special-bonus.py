import pandas as pd
import numpy as np

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    condition = (
        (employees["employee_id"] % 2 == 1) &
        (~employees["name"].str.startswith("M"))
    )
    
    employees["bonus"] = np.where(condition, employees["salary"], 0)
    
    return employees[["employee_id", "bonus"]].sort_values("employee_id")