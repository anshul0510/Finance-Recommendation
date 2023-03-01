from flask import Flask, jsonify, request
import pandas as pd
import recommendationEngine.impl.reccommendationImpl as rimpl
import recommendationEngine.impl.reccommendationImpl as fimp
import json
import os



app= Flask(__name__)


@app.route('/rcomEng', methods = ['GET'])
def getRecommendedServiceProvider():
   args = request.args 
   categoryFromMethod=rimpl.getRecommendedServiceProviders(args.get("category"), args.get("country"), args.get("avgRating"), args.get("noOfRatings"), args.get("quotedprice"), args.get("onTimeDelivery"), args.get("conflict"), args.get("pastExperience"))
   print(type(categoryFromMethod))
   return jsonify(categoryFromMethod.to_dict())


@app.route('/financer', methods = ['GET'])
def financer_providers():
   args = request.args
   financer = fimp.finance_service_provider(args.get("category"), args.get("country_of_operation"), args.get("avg_ratings"), args.get("experience"), args.get("services_offered"))
   print(type(financer))
   
   return jsonify(financer.to_dict())



@app.route('/fileconversion', methods = ['POST'])
def financer_recommenddation_provider():
    json_data = request.data
    data = json.loads(json_data)
    df = pd.DataFrame(data)
    df.to_csv('file.csv', index=False)
    args = request.args
    financer = fimp.finance_service_provider(args.get("category"), args.get("country_of_operation"), args.get("avg_ratings"), args.get("experience"), args.get("services_offered"))
    file_path = "file.csv"
    if os.path.exists(file_path):
        os.remove(file_path)
        print("File deleted successfully.")
    else:
        print("The file does not exist.")
    print(type(financer))
    return jsonify(financer.to_dict())




if __name__== "__main__":
    app.run(debug=True)



#http://127.0.0.1:5000/rcomEng?category=KYC&country=IN&avgRating=4&noOfRatings=100&quotedprice=200&onTimeDelivery=5&conflict=0&pastExperience=11

#http://127.0.0.1:5000/financer?category=SYNDICATE_FINANCE&avg_ratings=8&country_of_operation=IN&experience=1&services_offered=89
