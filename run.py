import argparse
import os

import pandas as pd

from src.scrapper.steam_scraper import steamScrapper


def main(game_id: int):
    
    myScrapper = steamScrapper()
    
    reviews_list = myScrapper.get_reviews(game_id=game_id)
    
    total_num_reviews = reviews_list[0]['query_summary']['total_reviews']
    assert len(reviews_list) == total_num_reviews//100 + 2* (total_num_reviews%100 != 0), f'There should be {total_num_reviews} reviews'
        
    df_reviews_list = [pd.DataFrame.from_dict(i['reviews']) for i in reviews_list] 
    df = pd.concat(df_reviews_list) 
    
    current_folder = os.path.dirname(__file__)
    
    path_data = os.path.join(current_folder, 'data') 
    path_data_raw = os.path.join(path_data, 'raw')
    
    try:
        os.mkdir(path_data)
    except FileExistsError:
        print('Folder "data" already exists')
        
    try:
        os.mkdir(path_data_raw)
    except FileExistsError:
        print('Folder "raw" already exists')
    
    
    game_name = myScrapper.get_name(game_id)
    df.to_csv(os.path.join(path_data_raw, f'{game_name}_reviews.csv'))

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("game_id", help="Game id according to steam", type=int)
    
    args = parser.parse_args()
    
    main(game_id=args.game_id)