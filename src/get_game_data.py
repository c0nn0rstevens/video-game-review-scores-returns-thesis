from data_sources.igdb.authentication import AuthIGDB
from data_sources.igdb.request import Request

# Instantiate auth object
auth = AuthIGDB()

# Authenticate with credentials
auth.authenticate()

# Print time until needing to re-authenticate.
auth.time_to_expiration("minutes")

games_url = "https://api.igdb.com/v4/games"
headers = {
    "Client-ID": auth.client_id,
    "Authorization": "Bearer " + auth.access_token,
    "Content-Type": "text/plain",
}

# Get apicalypse query from txt file.
with open("./src/data_sources/igdb/apicalypse_queries/games_query.txt", "r") as file:
    games_payload = file.read()

# Instantiate request object for games.
games_request = Request(url=games_url, headers=headers, payload=games_payload)

# Make the post request
games_request.post_request()

# Flatten the json response into a dataframe.
games_request.flatten_response()

# Save dataframes as csv.
games_request.request_dataframe.to_csv("games.csv")
