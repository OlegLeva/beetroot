import asyncio
import json
import random


async def client():
    while True:
        reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
        message = input()
        # print(f'Send to server: {message}')
        user_number = (random.randint(1, 1000))
        data = json.dumps({'sender': f'user:{int(user_number)} ', 'message': message})
        writer.write(data.encode())
        data = await reader.read(100)
        if data:
            print(f'Received: {data.decode()}')
            await asyncio.sleep(1)


asyncio.run(client())
