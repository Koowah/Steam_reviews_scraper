# TO DO
import os

from src import ROOT_DIR

class fileLogger():
    def __init__(self, game_id) -> None:
        self.game_id = game_id
        
    def make_folders(self) -> None:
        path_data = os.path.join(ROOT_DIR, 'data') 
        path_data_raw = os.path.join(path_data, 'raw')
        
        try:
            os.mkdir(path_data)
        except FileExistsError:
            print('Folder "data" already exists')
            
        try:
            os.mkdir(path_data_raw)
        except FileExistsError:
            print('Folder "raw" already exists')
            
    def make_csv(self, myScrapper, df):
        # df - dataframe containing data
        # myScrapper - steamScrapper
        
        game_name = myScrapper.get_name(self.game_id)
        df.to_csv(os.path.join(os.path.join(ROOT_DIR, 'data/raw'), f'{game_name}_reviews.csv'))
