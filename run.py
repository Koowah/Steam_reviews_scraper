import argparse
import os

import pandas as pd

from src.file_logger.file_logger import fileLogger
from src.scrapper.steam_scraper import steamScrapper


def main(game_id: int):
    
    myScrapper = steamScrapper()
    
    reviews_list = myScrapper.get_reviews(game_id=game_id)
    
    total_num_reviews = reviews_list[0]['query_summary']['total_reviews']
    assert len(reviews_list) == total_num_reviews//100 + 2* (total_num_reviews%100 != 0), f'There should be {total_num_reviews} reviews'
        
    df_reviews_list = [pd.DataFrame.from_dict(i['reviews']) for i in reviews_list] 
    df = pd.concat(df_reviews_list) 
    
    file_logger = fileLogger(game_id=game_id)
    file_logger.make_folders() # create data folder and subfolders
    file_logger.make_csv(myScrapper=myScrapper, df=df) # puts data into csv inside data/raw folder
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("game_id", help="Game id according to steam", type=int)
    
    args = parser.parse_args()
    
    main(game_id=args.game_id)