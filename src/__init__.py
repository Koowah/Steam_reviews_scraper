import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
BASE_URL = "https://store.steampowered.com/app/{}/"
REVIEWS_URL = "https://store.steampowered.com/appreviews/{}?\
        json=1&date_range=all&review_type=all&filter=recent&num_per_page=100&cursor={}"