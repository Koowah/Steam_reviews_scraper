import urllib.parse
import requests 
import time 
import json 

from bs4 import BeautifulSoup

from src import BASE_URL, REVIEWS_URL


class steamScrapper:
    
    def __init__(self, base_url: str = BASE_URL)-> None:
        self.base_url = base_url
    
    def get_name(self, game_id: int):
        url = BASE_URL.format(game_id)
        response = requests.get(url)
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')
        game_name = soup.find('div', {'id':"appHubAppName"}).text
    
        return game_name.replace(' ', '_')
    
    def get_url(self, cursor: str, game_id: int):
        return REVIEWS_URL.format(game_id, cursor)

    def get_json(self, cursor:str, game_id: int) -> dict:
        link = self.get_url(cursor, game_id)
        response = requests.get(link)
        response.encoding = 'utf-8-sig'
        data = response.text
        
        return json.loads(data)

    def get_next_cursor(self, data: dict):
        return urllib.parse.quote(data['cursor']) 

    def get_reviews(self, game_id: int) -> list:
        initial_cursor = '*' # according to steam doc
        
        data = self.get_json(initial_cursor, game_id)
        reviews_list = [data]

        i = 0
        while reviews_list[i]['reviews'] != []:
            try:
                next_cursor = self.get_next_cursor(reviews_list[i])
                next_data = self.get_json(next_cursor, game_id)

                reviews_list.append(next_data)
                i += 1
            except:
                print('Paying our respects to the server...')
                time.sleep(5)
                continue
                
        return reviews_list
