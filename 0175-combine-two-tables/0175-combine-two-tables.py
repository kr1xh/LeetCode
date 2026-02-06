import pandas as pd

def combine_two_tables(Person: pd.DataFrame, Address: pd.DataFrame) -> pd.DataFrame:
    return Person.merge(
        Address,
        on="personId",
        how="left"
    )[["firstName", "lastName", "city", "state"]]
