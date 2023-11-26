# TASK: Create a function which receive a pandas dataframe and a number of row wanted as parameter and returns a sample corresponding number of row from parameter #2.
import pandas as pd
def my_pandas_journey_return_n_sample_rows(df,nb_of_row):
    return df.head(nb_of_row)
