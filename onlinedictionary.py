import urllib.request
import json
import pprint

# TODO: replace with your own app_id and app_key
app_id = '460380f7'
app_key = '9a51e55a9cb3f1775de741264d0578a3'

language = 'en'
word_id = input('Enter a word to find its synonyms:')

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower() + '/synonyms;antonyms'

req = urllib.request.Request(url, headers = {'app_id': app_id, 'app_key': app_key})

try:
    req = urllib.request.urlopen(req).read()
    json_data = json.loads(req.decode('utf-8'))
    print('The synonyms of ' + word_id + ' are')
    for item in json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['subsenses'][0]['synonyms']:
        print(item['text'])
except urllib.error.HTTPError  as e:
    requrl = url
    print(str(e.code) + ' "' + word_id + '" not found')
