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
        comment_lst.append(comment['body'].decode('utf-8'))
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
        comment_lst.append(comment['body'].decode('utf-8'))
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
        comment_lst.append(comment['body'].decode('utf-8'))
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

'''
event_loop = asyncio.get_event_loop()
try:
    event_loop.create_task(second_post())
    event_loop.create_task(first_post())
    event_loop.create_task(third_post())
except Exception as e:
    print(e)
finally:
    event_loop.close()'''

# async def main():
#     task1 = asyncio.create_task(second_post())
#
#
#     await asyncio.gather(task1)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())

# pprint(res['data'][0]['body'])
# pprint(res['data'][1]['body'])
# print(res['data'][0]['body'])


# import pdb; pdb.set_trace()
