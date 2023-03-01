import os
import pandas as pd
import numpy as np
import json
from flask import Flask, jsonify, request
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def initializing_vectors(df1, df2):
        totaldesc=pd.concat([df2,df1], ignore_index=True)
        tfidf = TfidfVectorizer(stop_words="english")
        tfidf_matrix = tfidf.fit_transform(totaldesc)
        tfidf_matrix.shape
        cosine_similarity = linear_kernel(tfidf_matrix,tfidf_matrix)
        return cosine_similarity

def getting_similar_values(df1,df2, data):
        cosine_similarity = initializing_vectors(df1,df2)
        similarity_scores = list(enumerate(cosine_similarity[-1]))
        similarity_scores = sorted(similarity_scores,key =lambda x:x[1],reverse= True )
        similarity_scores = similarity_scores[1:6]
        indices = [i[0]for i in similarity_scores]
        return data.iloc[indices]

def gettingUsefulvalues(category , country_of_operation, avg_ratings, experience, services_offered):

    data=pd.read_csv("/Users/anshulbhardwaj/Desktop/financer_recommendation/RecommendationEngine/recommendationEngine/resources/Financer_Dataset.csv")
    #data = pd.read_csv("file.csv")
    print(data)
    New_values =data['avg_ratings'].apply(str) +' '+data['country_of_operation'].apply(str) + ' ' + data['category'].apply(str) +' '+ data['experience'].apply(str)+' '+ data['services_offered'].apply(str)
    print(New_values)
    data_testing = np.array([avg_ratings, country_of_operation, experience, category, services_offered])
    series_values = pd.Series(data_testing)
    data1=getting_similar_values(series_values,New_values,data)
    data2=data1['member_id']
    print(data2)
    return data2



