import requests
import json
from LinkedList import *

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
def populate_food_type_lst():
    food_type_lst = LinkedList()
    for business in businesses:
        food_type_lst.add_to_the_end([business["categories"][0]['title']])
    return food_type_lst


def populate_food_detail_lst():
    restaurants_dat_lst = LinkedList()
    for business in businesses:
        restaurants_dat_lst.add_to_the_end([business["name"], business["rating"], business.get("price"),
                                            business["location"]["display_address"], business["is_closed"]])
    return restaurants_dat_lst


food_types = populate_food_type_lst()
restaurants_info = populate_food_detail_lst()
food_types.show_list()
print("\n\n")
restaurants_info.show_list()
