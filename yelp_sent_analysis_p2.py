import pandas as pd
import requests
from requests.exceptions import HTTPError
import re

# Read file function to read the .txt files.
def read_file(name, ext):
    if ext.lower() == 'txt':
        with open(name, mode='r') as txt_file:
            file = txt_file.readlines()
            words = [line.rstrip('\n') for line in file]
            return words
    else:
        print(f"Unhandled file format {ext}. Please use either .txt or .csv file to use this function")

# Question 1: Ingest the positive words into a single list
pos_words = read_file('positive_words.txt', 'txt')

# Question 2: Ingest the negative words into a single list
neg_words = read_file('negative_words.txt', 'txt')

# Question 3 & 4: Open & parse the csv file for reading
yelp_input_file_df = pd.read_csv('yelp_dentists.csv', header=0, encoding = 'ascii', engine='python')

biz_id_list = []
review_list = {}

# Prepare a business id list that can be used to iterate through to get the reviews from yelp.
biz_id_list.append([f'"{row}"' for row in yelp_input_file_df["Business_ID"]])

# Question 5: for each business, use Yelp’s GraphQL reviews query API to return the business’ review text
def get_review(business_id, req_count):
    # Declare some str vars to hold immutable URLs
    YGQL_URL = 'https://api.yelp.com/v3/graphql'

    '''
    STEP 1: Request a Client ID and Client Secret from FatSecret
    '''
    API_KEY = '<<Secret>>'

    '''
    Step 2. Using the API key to call an YGQL Endpoint
    '''
    headers = {
        # combine the strings  'Bearer' and API key
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/graphql',
        'Accept-Language': 'en_US',
    }
    # Variable to hold graphql query to be passed to Yelp Review API
    review_graph_query = r'''
    {
      reviews(business: '''+business_id+''') {
        review {
          text
        }
      }
    }
    '''

    try:
        response = requests.post(YGQL_URL, data=review_graph_query, headers=headers)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print(f'POST Success for Request: {req_count}!')

    # deserialize the JSON payload
    json_data_dict = response.json()

    str_list = []
    for r in json_data_dict['data']['reviews']['review']:
        for v in r.values():
            str_list.append(v)
        review_list[business_id] = str_list

    return review_list

positive_review_list = {}
negative_review_list = {}
# Function to count positive and negative words in the review list.
def count(review_list, pos_words, neg_words):
    for id, review in review_list.items():
        word_list, unq_set = [], []
        for r in review:
            # Substitute the dots with space before splitting the words to list so we don't lose matches due to dots...
            str = re.sub(r'\.+', " ", r)
            word_list.append(str.strip().rstrip('!').split())
            [unq_set.extend(wl) for wl in word_list]
        pos_matches = set(unq_set).intersection(pos_words)
        neg_matches = set(unq_set).intersection(neg_words)
        positive_review_list.update({id: len(pos_matches)})
        negative_review_list.update({id: len(neg_matches)})

# Variable to hold req_count = 1 so when the program runs we know how many requests to Yelp API, has completed
req_count = 1
# Loop through each biz_id and get review by connecting to yelp and calling yelp Reviews API.
for biz_id in biz_id_list:
    for id in biz_id:
        reviews = get_review(id, req_count)
        req_count += 1
        # Function call to address requirement 6. For each business, record the (a) count of positive words
        # and (b) count of negative words occurring across all reviews for that business
        count(reviews, pos_words, neg_words)

# Sort the list in descending to find most positive and negative reviews.
sorted(positive_review_list.items(), key= lambda t: t[1], reverse=True)
sorted(negative_review_list.items(), key= lambda t: t[1], reverse=True)

highest_positive_reviews = {}
highest_negative_reviews = {}

# Below variables and two for loops are to handle ties i.e if multiple business has same count of positive and negative reviews.
highest_pos, highest_neg = max(positive_review_list.values()), max(negative_review_list.values())
for k, v in positive_review_list.items():
    if v == highest_pos:
        highest_positive_reviews.update({k:v})

for k, v in negative_review_list.items():
    if v == highest_neg:
        highest_negative_reviews.update({k:v})

p = {}
n = {}
# Pull the Business Name(s) for the highest positive & Negative reviews using the business ID.
for i in highest_positive_reviews.keys():
    p[i] = yelp_input_file_df.query(f'Business_ID == {i}')['Dentist_Name']

for i in highest_negative_reviews.keys():
    n[i] = yelp_input_file_df.query(f'Business_ID == {i}')['Dentist_Name']

# Print the final out as expected in the assignment. The for loops is to handle if multiple businesses has same number of positive and negative review words.
print(f'The reviews for Business Id(s): {[k for k in highest_positive_reviews.keys()]}, Business Name: {[i[1] for k, v in p.items() for i in v.items()]}'
      f' contained the most positive words with {[list(highest_positive_reviews.values())[0]]} positive word(s).')
print(f'The reviews for Business Id(s): {[k for k in highest_negative_reviews.keys()]}, Business Name: {[i[1] for k, v in n.items() for i in v.items()]}'
      f' contained the most negative words with {[list(highest_negative_reviews.values())[0]]} negative word(s).')

