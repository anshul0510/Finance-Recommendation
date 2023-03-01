
import recommendationEngine.model.recomendationModel as recomModel
import recommendationEngine.model.financerrecommendation as finModel


    
def getRecommendedServiceProviders(category , country, avgRating, noOfRatings, quotedprice, onTimeDelivery, conflict, pastExperience):
    recommendedServiceProviders=recomModel.findRecommendedMember(category , country, avgRating, noOfRatings, quotedprice, onTimeDelivery, conflict, pastExperience)
    return recommendedServiceProviders

def finance_service_provider(category , country_of_operation, avg_ratings, experience, services_offered):
    finance_service_provider = finModel.gettingUsefulvalues(category , country_of_operation, avg_ratings, experience, services_offered)
    
    return finance_service_provider
