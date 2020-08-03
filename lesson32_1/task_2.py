from aiohttp_requests import requests
import asyncio
import json

com_lst = []


async def second_post():
    await asyncio.sleep(0.1)
    resp = await requests.get('https://api.pushshift.io/reddit/comment/search/',
                              params={'subreddit': 'interestingasfuck', 'size': 25, 'sort': 'new'})

    res = await resp.json()
    comment_lst = []
    for comment in res['data']:
        comment_lst.append(comment['body'].encode())
    key_lst = list(range(1, 26))
    my_dict = dict(zip(key_lst, comment_lst))
    return com_lst.append(my_dict)


async def first_post():
    await asyncio.sleep(0.1)
    resp = await requests.get('https://api.pushshift.io/reddit/comment/search/',
                              params={'subreddit': 'nextfuckinglevel', 'size': 25, 'sort': 'new'})

    res = await resp.json()
    comment_lst = []
    for comment in res['data']:
        comment_lst.append(comment['body'].encode())
    key_lst = list(range(1, 26))
    my_dict = dict(zip(key_lst, comment_lst))
    return com_lst.append(my_dict)


async def third_post():
    await asyncio.sleep(0.1)
    resp = await requests.get('https://api.pushshift.io/reddit/comment/search/',
                              params={'subreddit': 'Minecraft', 'size': 25, 'sort': 'new'})

    res = await resp.json()
    comment_lst = []
    for comment in res['data']:
        comment_lst.append(comment['body'].encode())
    key_lst = list(range(1, 26))
    my_dict = dict(zip(key_lst, comment_lst))
    return com_lst.append(my_dict)


with open('comment_json.json', 'wb') as file:
    json.dump(com_lst, file, indent=4)


async def main():
    task1 = asyncio.create_task(second_post())
    task2 = asyncio.create_task(first_post())
    task3 = asyncio.create_task(third_post())

    await asyncio.gather(task1, task2, task3)


if __name__ == '__main__':
    asyncio.run(main())

