from data_sources.igdb.authentication import AuthIGDB
from igdb.wrapper import IGDBWrapper


def main():
    auth = AuthIGDB()
    auth.authenticate()
    print(
        "Token has " + str(auth.access_token_expire_time / 3600) + " hours remaining."
    )
    wrapper = IGDBWrapper(auth.client_id, auth.access_token)

    from igdb.igdbapi_pb2 import GameResult

    byte_array = wrapper.api_request(
        "games.pb",  # Note the '.pb' suffix at the endpoint
        "fields id, name; offset 0; where platforms=48;",
    )
    games_message = GameResult()
    games_message.ParseFromString(byte_array)


if __name__ == "__main__":
    main()
