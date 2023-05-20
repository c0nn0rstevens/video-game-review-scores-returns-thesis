from src.data_sources.igdb.request import Request
from src.data_sources.igdb.authentication import AuthIGDB


def test_post_request():
    test_auth = AuthIGDB()
    test_auth.authenticate()

    test_request = Request(
        url="https://api.igdb.com/v4/games",
        headers={
            "Content-Type": "text/plain",
            "Authorization": "Bearer " + test_auth.access_token,
            "Client-ID": test_auth.client_id,
        },
        payload="fields name; limit 10;",
    )
    # Get data and store it in the Request object.
    test_request.post_request()

    # Check that the response is stored as a json.
    assert isinstance(test_request.response_json[0], dict)
