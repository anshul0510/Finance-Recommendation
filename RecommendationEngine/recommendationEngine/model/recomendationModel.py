
import os
import pandas as pd
import numpy as np
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
#import recommendationEngine.config



# for Reference 
 #avgRating = '4'
    #noOfRatings='100'
    #quoted_price='200'
    #service_category='KYC'
    #onTimeDelivery='5'
    #conflict='0'
    #pastExperience='11'
    
def findRecommendedMember(category , country, avgRating, noOfRatings, quotedprice, onTimeDelivery, conflict, pastExperience):
    service_category=category
    data=pd.read_csv("/Users/anshulbhardwaj/Desktop/pull/RecommendationEngine/recommendationEngine/resources/recommendationSystem.csv")
    print(data)
    totalDescriptions =data['avgRatings'].apply(str) +' '+data['noOfRatings'].apply(str) + ' ' + data['quoted_price'].apply(str) +' '+ data['service_category']+' '+ data['onTimeDelivery'].apply(str)+' '+ data['conflict'].apply(str)+' '+ data['pastExperience'].apply(str)
    print(totalDescriptions)
    data_testing = np.array([avgRating, noOfRatings, quotedprice, service_category, country, onTimeDelivery, conflict, pastExperience])
    newDescription = pd.Series(data_testing)
    print(data_testing)
    data1=getRecommendation(newDescription,totalDescriptions,data)
    print(data1)
    data2=data1['serviceProviderUID']
    print(data2)
    return data2

def createMatrixForSimilarity(newdesc, totaldesc):
        totaldesc=pd.concat([totaldesc,newdesc], ignore_index=True)
        tfidf = TfidfVectorizer(stop_words="english")
        tfidf_matrix = tfidf.fit_transform(totaldesc)
        tfidf_matrix.shape
        cosine_similarity = linear_kernel(tfidf_matrix,tfidf_matrix)
        return cosine_similarity

def getRecommendation(newdesc,totaldesc, data):
        cosine_similarity = createMatrixForSimilarity(newdesc,totaldesc)
        similarity_scores = list(enumerate(cosine_similarity[-1]))
        similarity_scores = sorted(similarity_scores,key =lambda x:x[1],reverse= True )
        similarity_scores = similarity_scores[1:5]
        indices = [i[0]for i in similarity_scores]
        return data.iloc[indices]

def jsonToCsv(jsonFile):
    df = pd.read_json(jsonFile)
    return df.to_csv('file.csv')



def deleteCsvFile(csvFile):
    if(os.path.exists(csvFile) and os.path.isfile(csvFile)):
        os.remove(csvFile)
        print("file deleted")
    else:
        print("file not found")

def getServiceProviderDetails():
    #call api
    #getservices
    #getCompanies
    #getService deals
    #for same memberId aggregate the values

    serviceProviderDetails={}
    return serviceProviderDetails

