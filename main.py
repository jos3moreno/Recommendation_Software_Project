import requests 

YELP_END_POINT = "https://api.yelp.com/v3/businesses/search"
API_Key = "kc2UdKkJld9TTFN1aNDwn0jMxb8n8uHv__u_hDPXgih_PHowe9EAUp4Zo6QZYlySHncfOpN9iT8S95v18ldr2gYT7wULw10tMuLXZXp-TyIk-Jcuv4RfoNT_qyqhYnYx"
HEADER = {'Authorization': 'bearer %s' % API_Key}
parameters = {
    'location': 'Poway'
}

# Stock API
response = requests.get(YELP_END_POINT, headers=HEADER, params=parameters)
response.raise_for_status()
data = response.json()['businesses'][0]['name']

# tun dictionary into a list
print(data)
