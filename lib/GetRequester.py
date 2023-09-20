# Import necessary modules
import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  # Use .content to get the response as bytes

    def load_json(self):
        response_body = self.get_response_body()
        try:
            data = json.loads(response_body.decode('utf-8'))  # Decode the bytes to a string
            return data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {str(e)}")
            return None

# Example usage:
if __name__ == "__main__":
    URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    JSON_STRING = '[\n  {\n    "name": "Daniel",\n    "occupation": "LG Fridge Salesman"\n  },\n  {\n    "name": "Joe",\n    "occupation": "Teacher"\n  },\n  {\n    "name": "Avi",\n    "occupation": "DJ"\n  },\n  {\n    "name": "Howard",\n    "occupation": "Mountain Legend"\n  }\n]'
    
    requester = GetRequester(URL)
    
    # Get the response body
    response_body = requester.get_response_body()
    print("Response Body:")
    print(response_body)

    # Load JSON data
    data = requester.load_json()
    if data is not None:
        print("\nJSON Data:")
        print(data)
