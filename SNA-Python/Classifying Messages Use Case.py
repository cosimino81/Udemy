# -*- coding: utf-8 -*-
"""
-----------------------------------------------------------------------------

             Social Media Analytics with Python
             Copyright : V2 Maestros @2016
                    
Code Samples :Classification Example

Classify messages using TF-IDF and Naive Bayes techniques
-----------------------------------------------------------------------------
"""
#Setup the home directory.
import os
os.chdir("C:\Users\kumaran\Dropbox\V2Maestros\Courses\Social Media Analytics\Python")

#The tweets are pre-extracted and stored in a CSV file
tweets_data = pd.read_csv("ClassificationTweets.csv")
tweets_data.dtypes
tweets_data.describe()
tweets_data.head()

#Text Preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer
corpus = tweets_data.TWEET
vectorizer = TfidfVectorizer(stop_words='english')
tfidf=vectorizer.fit_transform(corpus).todense()
tfidf.shape
tfidf

#Naive Bayes Classification
from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
import sklearn.metrics

predictors = tfidf
targets = tweets_data.LEAGUE

pred_train, pred_test, tar_train, tar_test  = \
  train_test_split(predictors, targets, test_size=.3)

pred_train.shape
pred_test.shape
tar_train.shape
tar_test.shape

#Build model on training data
classifier=GaussianNB()
classifier=classifier.fit(pred_train,tar_train)

#Predict on test data
predictions=classifier.predict(pred_test)

#Print confusion matrix
sklearn.metrics.confusion_matrix(tar_test,predictions)
sklearn.metrics.accuracy_score(tar_test, predictions)
sklearn.metrics.classification_report(tar_test, predictions)




