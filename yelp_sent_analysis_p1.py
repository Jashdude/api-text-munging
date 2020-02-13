import requests
import pandas as pd
from requests.exceptions import HTTPError


# Declare some str vars to hold immutable URLs
YGQL_URL = 'https://api.yelp.com/v3/graphql'

'''
STEP 1: Request a Client ID and Client Secret from FatSecret
'''
API_KEY = '<<TYPE YOUR SECRET>>'

'''
Step 2. Using the API key to call an YGQL Endpoint
'''
headers = {
    # combine the strings  'Bearer' and API key
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/graphql',
    'Accept-Language': 'en_US',
}

'''
Question 1 & Question 2:
 - Location is set to "Downtown, Pittsburgh, PA"
 - Use Limit argument to set the limit to 50
 - For question 2. use the "best_match" mode in the argument sort_by, to pull the search results.
'''

gql_query = r'''
{
  search(term: "dentist",
         location: "Downtown, Pittsburgh, PA",
         limit: 50,
         sort_by: "best_match"
         ) {
    total
    business {
      id
      name
      rating
      review_count
      location {
        address1
        city
        state
        country
      }
    }
  }
}
'''

try:
    response = requests.post(YGQL_URL, data=gql_query, headers=headers)
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('POST Success!')

# deserialize the JSON payload
json_data_dict = response.json()

# Target Business Attributes dictionary
biz_ratings_dict = {}

# Data Structure to be passed to Pandas Data Frame
yelp_dentist = {
                "Business_ID": [],
                "Dentist_Name": [],
                "Ratings": []
                }

# Question3: Pull only Business Object's name, rating and id attributes
for b in json_data_dict['data']['search']['business']:
    yelp_dentist["Business_ID"].append(b['id'])
    yelp_dentist["Dentist_Name"].append(b['name'])
    yelp_dentist["Ratings"].append(b['rating'])

# Create a Data Frame so that the data can be handled in 2-D
df = pd.DataFrame(yelp_dentist)
# Question4: Sort the search results on biz_rating in descending order
df.sort_values(['Ratings'], inplace=True, ascending=False)
# Question5: Output the captured information to a CSV file with name yelp_dentists.csv
df.to_csv("yelp_dentists.csv", index=None, header=True )
print("Successfully completed the program and exported the yelp_dentists.csv file to current folder")

