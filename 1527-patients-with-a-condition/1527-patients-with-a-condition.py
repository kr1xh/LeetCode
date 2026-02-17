import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    pattern = r'(^|\s)DIAB1'
    
    return patients[
        patients["conditions"].str.contains(pattern, regex=True, na=False)
    ][["patient_id", "patient_name", "conditions"]]