import requests
from data import *
import json

YELP_END_POINT = "https://api.yelp.com/v3/businesses/search"
BUSINESS_DETAILS = "https://api.yelp.com/v3/businesses/{id}"
API_Key = "kc2UdKkJld9TTFN1aNDwn0jMxb8n8uHv__u_hDPXgih_PHowe9EAUp4Zo6QZYlySHncfOpN9iT8S95v18ldr2gYT7wULw10tMuLXZXp-TyIk-Jcuv4RfoNT_qyqhYnYx"
HEADER = {'Authorization': 'bearer %s' % API_Key}
parameters = {
    'location': 'Poway'
}


response = requests.get(YELP_END_POINT, headers=HEADER, params=parameters)
response.raise_for_status()
data = json.loads(response.text)
businesses = data['businesses']


# print(businesses[0]["categories"][0]['alias'])
# Clean data from .json format into more readable form
# NOTE: the API returns 20 restaurants
for business in businesses:
    types_of_food.append([business["categories"][0]['title']])
    restaurants_data.append([business["name"], business["rating"], business.get("price"),
                             business["location"]["display_address"], business["is_closed"]])


# businesses_id: oxfQZ80ON1Dk1Lnq51EAjw  tYlETe8fXejtXTidRHlszg
# print(len(restaurants_data))
for i in range(len(restaurants_data)):
    print(f'${restaurants_data[i]} \n ${types_of_food[i]}')