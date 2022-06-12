import requests
import json
from LinkedList import *
from prettytable import PrettyTable
from data import *

YELP_END_POINT = "https://api.yelp.com/v3/businesses/search"
API_Key = "kc2UdKkJld9TTFN1aNDwn0jMxb8n8uHv__u_hDPXgih_PHowe9EAUp4Zo6QZYlySHncfOpN9iT8S95v18ldr2gYT7wULw10tMuLXZXp-TyIk-Jcuv4RfoNT_qyqhYnYx"
HEADER = {'Authorization': 'bearer %s' % API_Key}
parameters = {
    'location': 'Kerny Mesa'
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
        food_type_lst.add_to_the_end([business["categories"][0]['alias']])
    return food_type_lst


def populate_food_detail_lst():
    restaurants_dat_lst = LinkedList()
    for business in businesses:
        restaurants_dat_lst.add_to_the_end([business["name"], business["rating"], business.get("price"),
                                            business["location"]["address1"], business["phone"]])
    return restaurants_dat_lst


food_types = populate_food_type_lst()
restaurants_info = populate_food_detail_lst()


# This function will return the index location of the node where
# the user is looking for a food type with one char or 2, will return a dictionary
# with the food_type as key (doesn't allow duplicates) and a [] with the indices where
# food_type's are
def type_location_search(food_types_lst, char):
    if food_types_lst.is_empty():
        return
    current = food_types_lst.get_head_node()
    result = {}
    count = 0
    while current is not None:
        if str((current.get_value()[0])).startswith(char):
            result.setdefault(current.get_value()[0], []).append(count)
        current = current.next
        count += 1
    return result


chosen_food = ""

while len(chosen_food) == 0:
    user_input = str(input(
        "\nWhat do you feel like eating?\nEnter the beginning of the food: ")).upper()

    match_types = type_location_search(food_types, user_input)
    print(match_types)
    print("Here is what I found: ")
    # Create a table
    food_type_table = PrettyTable()
    food_type_table.field_names = ["Food Type", "Count"]
    for key, value in match_types.items():
        food_type_table.add_row([key, len(value)])
    print(food_type_table)

    if len(match_types) > 1:
        type_choice = str(input("What is your food type choice: "))
        print(f'You have enter: {type_choice}')
        user_continue = str(input("Do you want to continue: (enter 'y' for yes and 'n' for no): "))
        if user_continue == 'y':
            restaurants_table = PrettyTable()
            restaurants_table.field_names = ["Restaurant", "Rating", "Price", "Address", "Phone"]
            types = match_types[type_choice]
            for restaurants in types:
                restaurants_lst = (restaurants_info.get_node_by_value(restaurants))
                restaurants_table.add_row([restaurants_lst[0],
                                           restaurants_lst[1],
                                           restaurants_lst[2],
                                           restaurants_lst[3],
                                           restaurants_lst[4]])
            print(restaurants_table)
            # Ask user if they would like to search for more
            repeat = str(input("Do you want to continue your search: (enter 'y' for yes and 'n' for no) "))
            if repeat == 'y':
                selected_food_type = ""
            else:
                print("Hope I satisfy your craving.")
                quit()
