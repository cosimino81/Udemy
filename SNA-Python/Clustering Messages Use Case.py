# -*- coding: utf-8 -*-
"""
-----------------------------------------------------------------------------

             Social Media Analytics with Python
             Copyright : V2 Maestros @2016
                    
Code Samples :Clustering Example

Classify messages using TF-IDF and Naive Bayes techniques
-----------------------------------------------------------------------------
"""
#Setup the home directory.
import os
os.chdir("C:\Users\kumaran\Dropbox\V2Maestros\Courses\Social Media Analytics\Python")

#The tweets are pre-extracted and stored in a CSV file
tweets_data = pd.read_csv("ClusteringTweets.csv",
                          header=None)
tweets_data.dtypes
tweets_data.describe()
tweets_data.head()

#Text Preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer
corpus = tweets_data[0]
vectorizer = TfidfVectorizer(stop_words='english')
tfidf=vectorizer.fit_transform(corpus).todense()
tfidf.shape
tfidf

#Cluster into 3 clusters/groups

from sklearn.cluster import KMeans
model=KMeans(n_clusters=3)
model.fit(tfidf)
prediction=model.predict(tfidf)
prediction

for i in range(0, prediction.size ):
    print prediction[i], tweets_data[0][i]




