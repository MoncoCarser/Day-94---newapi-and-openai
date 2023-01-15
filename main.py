import os, requests, json, openai

#Replit's secrets contain the necessary keys received from newsapi and openai web pages
news_api = os.environ['news_api_key']
openai.organisation = os.environ['openai_organization_id']
openai.api_key = os.environ['openai_api_key']
#Model.list() returns information about all models available
openai.Model.list()

country = "fr" #we can choose what country gb / us / etc.
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={news_api}"

result = requests.get(url)
data = result.json()

# If there is an error in the API request, the code will exit
if result.status_code != 200:
    print("Failed to retrieve news articles. Error code: " + str(result.status_code))
    exit()

#if needed to print the news stories:
#print(data["articles"][0]["content"])

#below loops through 5 news, asks openai to summarize them, and returns the one sentence version
counter = 0
for article in data["articles"]:
    counter +=1
    if counter > 5:
        break
    #promt is the key to modify our request, like when asking Chat GPT to do something
    prompt = (f"Summarize {article['title']}, {article['content']} in one sentence.")
    response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=50)
    print(response["choices"][0]["text"].strip())
    print()