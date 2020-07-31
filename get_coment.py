import asyncio
from aiohttp_requests import requests
import requests

'''url = 'https://api.pushshift.io/reddit/comment/search/'
async def get_com(url, query):
    resp = await requests.get(url, params={'q': {query}})
    data = await resp.json()
    return data'''

'''url = 'https://api.pushshift.io/reddit/comment/search/'
def get_com(url, query):
    resp = requests.get(url, params={'q': {query}})
    data = resp.json()
    return data
print(get_com(url, "author",))'''

respon = requests.get('https://api.pushshift.io/reddit/comment/search/')
print(respon)

