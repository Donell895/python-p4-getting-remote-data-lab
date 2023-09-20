from lib.get_requester import GetRequester

# Create an instance of GetRequester with the URL
get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')

# Load JSON data from the URL
data = get_requester.load_json()

# Print the loaded JSON data
print(data)
