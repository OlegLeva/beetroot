from aiohttp_requests import requests
import asyncio
import json

com_lst = []


async def get_comment(topic):
    resp = await requests.get('http://api.pushshift.io/reddit/comment/search/',
                              params={'subreddit': topic, 'size': 25, 'sort': 'new'})
    res = await resp.json()
    comment_lst = []
    for comment in res['data']:
        comment_lst.append(comment['body'])
    key_lst = list(range(1, 26))
    my_dict = dict(zip(key_lst, comment_lst))
    com_lst.append(my_dict)


async def main():
    task1 = asyncio.create_task(get_comment('interestingasfuck'))
    task2 = asyncio.create_task(get_comment('nextfuckinglevel'))
    task3 = asyncio.create_task(get_comment('Minecraft'))

    await asyncio.gather(task1, task2, task3)


if __name__ == '__main__':
    asyncio.run(main())
    with open('comment_json.json', 'w') as file:
        json.dump(com_lst, file, indent=4)
