import pandas as pd
import numpy as np

""" This code specifies which labels we want """

data = pd.read_csv("demographic.csv")

#Change these for new labels
labels = data[['age','country','gender']]


""" Select between csv file with headers and index or not"""
#labels.to_csv('labels.csv')
#labels.to_csv('labels_without_header.csv',header=False, index = False)
