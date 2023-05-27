import requests
import pandas as pd


class Request:
    def __init__(self, url, headers, payload):
        self.url = url
        self.headers = headers
        self.payload = payload
        self.post_response = []
        self.response_list = []
        self.request_dataframe = None

    def post_request(self):
        # Keep requesting until list is empty
        list_empty_bool = False
        offset = 0

        while not list_empty_bool:
            # Store post response.
            response = requests.post(
                url=self.url,
                headers=self.headers,
                data=self.payload + "offset" + str(offset) + ";",
            )

            # Check if the last response was an empty dictionary. End loop if True.
            list_empty_bool = not (bool(response.json()))

            # Store response in post_response list.
            self.post_response.append(response)

            # Store response dictionary in response_dict.
            print(response.json())
            self.response_list += self.post_response[-1].json()

            # Offset by request size to avoid duplicates in responses.
            offset += 500

    def flatten_response(self):
        # Flatten json response into dataframe.
        self.request_dataframe = pd.json_normalize(self.response_list)

    def make_dataframe(self, cols):
        # First make a dataframe using the first dictionary in the list.
        self.request_dataframe = pd.DataFrame(columns=cols)

        # Loop through the rest of the dictionaries in the list and add them to
        # the dataframe.
        for count, dictionary in enumerate(self.response_list):
            # Create temporary dataframe for concatenating with the main df.
            df_temp = pd.DataFrame(dictionary, index=[count])

            # Join the request_dataframe with the temporary df.
            self.request_dataframe = pd.concat([self.request_dataframe, df_temp])
