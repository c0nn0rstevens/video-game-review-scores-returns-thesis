import os
from dotenv import load_dotenv
import requests
import time

# Load environment variables
load_dotenv()


# Class to hold authentication details.
class AuthIGDB:
    """
    Used for authentication with Twitch API before making requests to the IGDB
    game database.
    """

    def __init__(
        self, client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET")
    ) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.request_made_time = None
        self.access_token = None
        self.access_token_expire_time = None

    def authenticate(self) -> None:
        """
        Authenticate with Twitch API to get access token for making API calls.
        """

        AUTH_URL = (
            "https://id.twitch.tv/oauth2/token?client_id="
            + self.client_id
            + "&client_secret="
            + self.client_secret
            + "&grant_type=client_credentials"
        )
        REQUEST_TIME = int(time.time())

        # Request authentication.
        access_token_response = requests.post(AUTH_URL)

        # Store authentication response as dictionary.
        access_token_dict = access_token_response.json()

        try:
            self.access_token = access_token_dict["access_token"]

        except KeyError:
            print("Authentication failed. Access token not returned.")

        # Save access token.
        self.access_token = access_token_dict["access_token"]
        self.access_token_expire_time = REQUEST_TIME + int(
            access_token_dict["expires_in"]
        )

    def time_to_expiration(self, unit_of_measure):
        if unit_of_measure == "minutes":
            denominator = 60

        elif unit_of_measure == "hour":
            denominator = 3600

        elif unit_of_measure == "day":
            denominator = 85400

        else:
            print(
                "Please choose a valid unit of measure. 'minutes', 'hour' and "
                "'day' are valid inputs."
            )

        message = "Token has {hours_remaining: 2f} hours remaining."
        print(
            message.format(hours_remaining=self.access_token_expire_time / denominator)
        )
