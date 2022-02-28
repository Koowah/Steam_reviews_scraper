from bs4 import BeautifulSoup
import pandas as pd

import urllib.parse # to properly format urls
import requests # to make html requests
import time # to pay respects to the server
import json # /appreviews/ returns json formatted files

import os 


####################################################################
######################### Helper Functions #########################
####################################################################

# get game name from game ID - reverse function is also interesting
def get_name(game_id:str) -> str:
    url = f'https://store.steampowered.com/app/{game_id}/'
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    game_name = soup.find('div', {'id':"appHubAppName"}).text
    
    return game_name.replace(' ', '_')

# url format for steam reviews
def url(cursor:str, game_id:str) -> str:
    # filter has to be set to 'recent' to allow for iterative run through all reviews
    # would be cleaner to add url parameters as inputs to the function w/ proper explanation
    return f'https://store.steampowered.com/appreviews/{game_id}?json=1&date_range=all&review_type=all&filter=recent&num_per_page=100&cursor={cursor}'

# get data
def get_json(cursor:str, game_id:str) -> dict:
    link = url(cursor, game_id)
    response = requests.get(link)
    response.encoding = 'utf-8-sig'
    data = response.text
    
    return json.loads(data)

# get cursor field to find next url's cursor parameter
def get_next_cursor(data):
    return urllib.parse.quote(data['cursor']) # makes data['cursor'] url-friendly (which it isn't always)

# get reviews iterativlely
def get_reviews(game_id:str) -> list:
    initial_cursor = '*' # according to steam doc
    
    data = get_json(initial_cursor, game_id)
    reviews_list = [data]

    i = 0
    while reviews_list[i]['reviews'] != []:
        try:
            next_cursor = get_next_cursor(reviews_list[i])
            next_data = get_json(next_cursor, game_id)

            reviews_list.append(next_data)
            i += 1
        except:
            print('Paying our respects to the server ...')
            time.sleep(5)
            continue
            
    return reviews_list
