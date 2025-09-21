import requests

bearer_token = "AAAAAAAAAAAAAAAAAAAAAOAv4QEAAAAABHy8FrWqIFwC2CfyUswvFUFIx0A%3Des4mCbTTKJaasovyTXSHEdoawlCQonBVPVDGe6zlUxXAoliPst"

headers = {"Authorization": f"Bearer {bearer_token}"}
query = "flood lang:en -is:retweet"
url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&max_results=10"

response = requests.get(url, headers=headers)
print(response.json())
