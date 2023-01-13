import requests, json, os
import openai

news_api = os.environ['news_api_key']
country = "us"
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={news_api}"
#url = f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={news_api}"

openai.organization = os.environ['openai_organization_id']
openai.api_key = os.environ['openai_api_key']
openai.Model.list()




result = requests.get(url)
data = result.json()
#print(json.dumps(data, indent = 2))

for article in data["articles"]:
    print(article["title"])
    print()
    print(article["url"])
    print()
    print(article["content"])
    print()




prompt = "How many car brands exist?"

response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=6)

#print(response)
print(response["choices"][0]["text"].strip())