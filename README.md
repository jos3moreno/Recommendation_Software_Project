# Recommendation_Software_Project


This project works as follows:

1. Starts by calling the Yelp API to search for restaurants information. Then I used a LinkedList data structure to store the data.
2. There will be 2 linked list, one is called food_types, the data loaded into this LinkedList will be a dictionary. Within the dictionary 
  there will be the food type as key, the values will be a list of indices that indicate the occurrences. Later I used the indices to get data 
  from a second LinkedList. 
3. the second LinkedList will be loaded with a list containing restaurant relevant information such as; ['name', 'rating', 'cost', 'address', 'phone']
   
4. Data will be collected from the user to give him recommendations, the user can start by typing the initial of a food category if they do not 
  know what categories are there. For example, the user can choose to type ch for chinese or just c chinese. Another example, is the user can
  enter b, the categories display can be burgers, bbq, brunch, etc. wherever food types the yelp API replies back. 
  
5. Using the initial linked list with containing the food_type, the program will get data by indices from the restaurant_info LinkedList 
   and displayed to the user in a Prettytable()
   
6. NOTE: There is only one categery with starting with r and d

7. BUGS:  


![Screen Shot 2022-06-11 at 8 20 22 PM](https://user-images.githubusercontent.com/62624769/173212856-24a75761-0a07-41e0-b29d-17821d12aee6.png)

![Screen Shot 2022-06-11 at 8 20 33 PM](https://user-images.githubusercontent.com/62624769/173212861-c7409ff4-10c9-4a65-8976-3f171b9d46ac.png)
