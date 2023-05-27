from data_sources.igdb.authentication import AuthIGDB
from data_sources.igdb.request import Request

# Instantiate auth object
auth = AuthIGDB()

# Authenticate with credentials
auth.authenticate()

# Print time until needing to re-authenticate.
auth.time_to_expiration("minutes")

companies_url = "https://api.igdb.com/v4/companies"
games_url = "https://api.igdb.com/v4/games"
headers = {
    "Client-ID": auth.client_id,
    "Authorization": "Bearer " + auth.access_token,
    "Content-Type": "text/plain",
}

# Get apicalypse query from txt file.
with open("./src/companies_query.txt", "r") as file:
    companies_payload = file.read()

# Instantiate request object for companies.
companies_request = Request(
    url=companies_url, headers=headers, payload=companies_payload
)

# Make the post request
companies_request.post_request()

# Check the contents of the Request.response_list.
print(companies_request.response_list)

companies_request.flatten_response()

# Save dataframes as csv.
companies_request.request_dataframe.to_csv("game_companies.csv")
