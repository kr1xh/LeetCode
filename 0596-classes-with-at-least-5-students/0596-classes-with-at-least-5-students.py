import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    result = (
        courses
        .groupby("class")
        .size()
        .reset_index(name="count")
    )
    
    return result[result["count"] >= 5][["class"]]