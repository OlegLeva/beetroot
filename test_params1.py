import requests
import asyncio
from pprint import pprint

f = open('comment_json.json', 'wb')
f.close()


resp = requests.get('https://api.pushshift.io/reddit/comment/search/',
                          params={'subreddit': 'nextfuckinglevel', 'size': 25, 'sort': 'new'})

res = resp.json()
comment_lst = []
for comment in res['data']:
    comment_lst.append(comment['body'])
key_lst = list(range(1, 26))
my_dict = dict(zip(key_lst, comment_lst))
print((my_dict))


# pprint(res['data'][0]['body'])
# pprint(res['data'][1]['body'])
# print(res['data'][0]['body'])


# import pdb; pdb.set_trace()
