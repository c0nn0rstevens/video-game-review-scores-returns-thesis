from data_sources.igdb.authentication import AuthIGDB
from data_sources.igdb.request import Request


def main():
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

    with open("./src/games_query.txt", "r") as file:
        games_payload = file.read()

    # Instantiate request object for companies and games
    companies_request = Request(
        url=companies_url, headers=headers, payload=companies_payload
    )
    games_request = Request(url=games_url, headers=headers, payload=games_payload)

    # Make the post request
    companies_request.post_request()
    games_request.post_request()

    # Check the contents of the Request.response_list.
    print(companies_request.response_list)
    print(games_request.response_list)

    # Add all of the dictionaries in the list to a dataframe
    companies_request.make_dataframe(
        cols=[
            "id",
            "name",
            "start_date",
            "changed_company_id",
            "parent",
            "change_date",
        ]
    )
    games_request.make_dataframe(
        cols=[
            "id",
            "age_ratings",
            "aggregate_rating",
            "aggregate_rating_count",
            "first_release_date",
            "follows",
            "game_modes",
            "genres",
            "involved_companies",
        ]
    )

    # Save dataframe as csv.
    companies_request.request_dataframe.to_csv("game_companies.csv")

    #


if __name__ == "__main__":
    main()
