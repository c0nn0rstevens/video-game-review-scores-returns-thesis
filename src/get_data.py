from data_sources.igdb.authentication import AuthIGDB
import requests


def main():
    auth = AuthIGDB()
    auth.authenticate()
    print(
        "Token has " + str(auth.access_token_expire_time / 3600) + " hours remaining."
    )
    wrapper = IGDBWrapper(auth.client_id, auth.access_token)

    from igdb.igdbapi_pb2 import GameResult

    byte_array = wrapper.api_request(
        "companies.pb",  # Note the '.pb' suffix at the endpoint
        "fields name, parent, start_date;where published.first_release_date >= 970397863;",
    )
    games_message = GameResult()
    games_message.ParseFromString(byte_array)
    print(games_message.ListFields)


if __name__ == "__main__":
    main()
