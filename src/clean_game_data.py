# First run src/data_sources/get_game_data.py to get the csv in your working directory.
import pandas as pd

# Import csv into dataframe.
raw_games_df = pd.read_csv("games.csv")
