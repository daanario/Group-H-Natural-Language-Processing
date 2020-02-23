
import pandas as pd

""" This trims the data down to the relevant part """

data = pd.read_csv("cleaned_hm.csv")

relevant_data = data[['cleaned_hm']]

""" You choose between a dataframe with or without header and index """
#relevant_data.to_csv("trimmed_data_with_header_and_index.csv")
#relevant_data.to_csv("trimmed_data_no_header_or_index.csv", header = False, index = False)
