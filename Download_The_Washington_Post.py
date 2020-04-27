import requests
import json
from tqdm import tqdm 
# url = "https://sitesearchapp.washingtonpost.com/sitesearch-api/v2/search.json?count=40&datefilter=displaydatetime:%5BNOW%2FDAY-60DAYS+TO+NOW%2FDAY%2B1DAY%5D&facets.fields=%7B!ex%3Dinclude%7Dcontenttype,%7B!ex%3Dinclude%7Dname&filter=%7B!tag%3Dinclude%7Dcontenttype:(%22Article%22)&highlight.fields=headline,body&highlight.on=true&highlight.snippets=1&query=coronavirus&sort=&spellcheck=true&startat=40&callback=angular.callbacks._2"
# url="https://sitesearchapp.washingtonpost.com/sitesearch-api/v2/search.json?count=500&datefilter=displaydatetime:%5BNOW%2FDAY-60DAYS+TO+NOW%2FDAY%2B1DAY%5D&facets.fields=%7B!ex%3Dinclude%7Dcontenttype,%7B!ex%3Dinclude%7Dname&filter=%7B!tag%3Dinclude%7Dcontenttype:(%22Article%22)&highlight.fields=headline,body&highlight.on=true&highlight.snippets=1&query=coronavirus&sort=&spellcheck=true&startat=0"
for i in tqdm(range(0,600,1)):
    
#     url='https://sitesearchapp.washingtonpost.com/sitesearch-api/v2/search.json?count=20&datefilter=displaydatetime:%5BNOW%2FDAY-60DAYS+TO+NOW%2FDAY%2B1DAY%5D&facets.fields=%7B!ex%3Dinclude%7Dcontenttype,%7B!ex%3Dinclude%7Dname&filter=%7B!tag%3Dinclude%7Dcontenttype:(%22Article%22)&highlight.fields=headline,body&highlight.on=true&highlight.snippets=1&query=coronavirus&sort=&startat={}'.format(i*20)
    url='https://sitesearchapp.washingtonpost.com/sitesearch-api/v2/search.json?count=20&datefilter=displaydatetime:%5BNOW%2FDAY-1YEAR+TO+NOW%2FDAY%2B1DAY%5D&facets.fields=%7B!ex%3Dinclude%7Dcontenttype,%7B!ex%3Dinclude%7Dname&filter=%7B!tag%3Dinclude%7Dcontenttype:(%22Article%22)&highlight.fields=headline,body&highlight.on=true&highlight.snippets=1&query=coronavirus&sort=&startat={}'.format(i*20)
    res = requests.get(url=url)
    print(i*20)
    # print(res.text)
    json_data=json.loads(res.text)
#     print(json_data)
    if(not json_data['results']['documents']):
            continue
    print(len(json_data['results']['documents']))

    with open('./data/washingtonpost_{}.json'.format(i), 'w') as json_file:
        json_file.write(res.text)

print("Done")