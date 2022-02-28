from steam_scraper import *

####################################################################
########################### Main Program ###########################
####################################################################


def main(game_id=678950): # game_id 678950 for DBZ FighterZ - get it from steam or steamdb
    
    ################### Download all reviews for the game ###################
    reviews_list = get_reviews(game_id)
    
    ################### Make sure we downloaded all reviews ###################
    # total_num_reviews//100 gives us the number of entries with the full 100 reviews (per query)
    # if total_num_reviews%100 != 0 we need to add on entry for the last < 100 reviews
    # and one last empty entry (which ends iterative run through reviews) hence the 2*
    total_num_reviews = reviews_list[0]['query_summary']['total_reviews']
    assert len(reviews_list) == total_num_reviews//100 + 2* (total_num_reviews%100 != 0), f'There should be {total_num_reviews} reviews'
        
    ################### Put data in dataframe ###################
    df_reviews_list = [pd.DataFrame.from_dict(i['reviews']) for i in reviews_list] # list of dict to list of dfs
    df = pd.concat(df_reviews_list) # concatenates all dfs into one big df
    
    ################### Save to CSV ###################
    # get current folder's absolute path
    current_folder = os.path.dirname(__file__)
    
    # define paths of necessary folders
    path_data = os.path.join(current_folder, 'data') 
    path_data_raw = os.path.join(path_data, 'raw')
    
    # make folders
    try:
        os.mkdir(path_data)
    except FileExistsError:
        print('Folder "data" already exists')
        
    try:
        os.mkdir(path_data_raw)
    except FileExistsError:
        print('Folder "raw" already exists')
    
    
    # then save the csv file inside relevant folder - /data/raw
    game_name = get_name(game_id)
    df.to_csv(os.path.join(path_data_raw, f'{game_name}_reviews.csv'))

    
if __name__ == '__main__':
    main()