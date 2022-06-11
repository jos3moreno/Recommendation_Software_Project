'''
for business in businesses:
    types_of_food.append([business["categories"][0]['title']])
    restaurants_data.append([business["name"], business["rating"], business.get("price"),
                             business["location"]["display_address"], business["is_closed"]])
'''
types_of_food = []

restaurants_data = []
'''
["Smokin J's BBQ", 4.5, '$$', ['14035 Midland Rd', 'Poway, CA 92064'], False]
['Baba Kabob', 4.5, None, ['13538 Poway Rd', 'Ste C', 'Poway, CA 92064'], False]
['Don Pollo', 4.5, '$$', ['13338 Poway Rd', 'Poway, CA 92064'], False]
['In The Mix Yogurt', 4.5, '$', ['13450 Poway Rd', 'Poway, CA 92064'], False]
['Wholly Crepe', 4.5, '$$', ['14045 Midland Rd', 'Poway, CA 92064'], False]
["Niko's Halo-Halo & Sari-Sari", 4.0, '$$', ['14034 Poway Rd', 'Ste C', 'Poway, CA 92064'], False]
['Sushi Lounge Poway', 4.0, '$$', ['12622 Poway Rd', 'Ste A', 'Poway, CA 92064'], False]
['Taco Taco Poway', 4.0, '$', ['13429 Community Rd', 'Poway, CA 92064'], False]
['Ichizen Sushi & Japanese Cuisine', 4.0, '$', ['13307 Poway Rd', 'Poway, CA 92064'], False]
['El Ranchito Taco Shop', 4.0, '$', ['13654 Poway Rd', 'Ste 10', 'Poway, CA 92064'], False]
['Greens Please Wellness Kitchen', 5.0, '$$', ['12202 Poway Rd', 'Ste 100', 'San Diego, CA 92064'], False]
['The Kings Craft Coffee', 4.5, '$', ['14530 Espola Rd', 'Ste A', 'Poway, CA 92064'], False]
['Tikka Lounge', 4.5, '$$', ['13513 Poway Rd', 'Poway, CA 92064'], False]
['Mount Woodson Trail', 4.5, None, ['14644 Lake Poway Rd', 'Poway, CA 92074'], False]
["Franco's Flapjack Family Restaurant", 4.0, '$$', ['14034 Poway Rd', 'Poway, CA 92064'], False]
["O'Brien's Boulangerie", 4.5, '$$', ['13615 Stowe Dr', 'Poway, CA 92064'], False]
['Mostra Coffee', 4.5, '$$', ['12045 Carmel Mountain Rd', 'Ste 302', 'San Diego, CA 92128'], False]
['Tong Sake House', 4.5, '$$', ['12320 Poway Rd', 'Poway, CA 92064'], False]
['The Boba Co', 4.0, '$', ['13526 Poway Rd', 'Ste A', 'Poway, CA 92064'], False]
['Iron Pan Thai Kitchen', 4.0, '$$', ['13538 Poway Rd', 'Ste A', 'Poway, CA 92064'], False]
'''
'''
[
    0. ['Barbeque']
    1. ['Mediterranean']
    2. ['Chicken Shop']
    3. ['Ice Cream & Frozen Yogurt']
    4. ['Creperies']
    5. ['Bubble Tea']
    6. ['Sushi Bars']
    7. ['Mexican']
    8. ['Japanese']
    9. ['Mexican']
    10. ['Juice Bars & Smoothies']
    11. ['Coffee Roasteries']
    12. ['Indian']
    13. ['Hiking']
    14. ['Breakfast & Brunch']
    15. ['Bakeries']
    16. ['Coffee Roasteries']
    17. ['Korean']
    18. ['Bubble Tea']
    19. ['Thai']    
]
'''

