import pandas as pd

""" The following reads the dataset and creates a sample list from it"""


#reading file
data = pd.read_csv("cleaned_hm.csv")

#only need the clean texts
relevant_data = data[['cleaned_hm']]

#changing from dataframe type to list of lists
list_sheet = relevant_data.values.tolist()

#limiting sample size to 100 rows
sample = list_sheet[0:100]

#creating list of strings from the list of lists
new_list = []
for element in sample:
    new_list.extend(element)

""" The following creates an array of count vectors. Default values used """
from sklearn.feature_extraction.text import CountVectorizer

#creating the count_vector
cv = CountVectorizer(new_list)
count_vector =cv.fit_transform(new_list)


""" The following upgrades from count vectorization to TF-IDF """

from sklearn.feature_extraction.text import TfidfTransformer

#computing idf values
tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transformer.fit(count_vector)

#creating tfidf count vector
new_count_vector=cv.transform(new_list)
tf_idf_vector=tfidf_transformer.transform(count_vector)


#tf_idf_vector.toarray()
