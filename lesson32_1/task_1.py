import asyncio


async def fib():
    await asyncio.sleep(1)
    lst_fib = []
    a, b = 0, 1
    for i in range(10):
        a, b = b, a + b
        lst_fib.append(a)
    print(lst_fib)


async def factorial():
    await asyncio.sleep(1)
    fac, i = 1, 0
    lst_fac = []
    for m in range(10):
        while i < m:
            i += 1
            fac = fac * i
            lst_fac.append(fac)
    print(lst_fac)


async def sqrt():
    await asyncio.sleep(1)
    lst_sqrt = []
    for i in range(10):
        s = i ** 2
        lst_sqrt.append(s)
    print(lst_sqrt)


async def cubic():
    await asyncio.sleep(1)
    lst_cub = []
    for i in range(10):
        s = i ** 3
        lst_cub.append(s)
    print(lst_cub)


async def main():
    task1 = asyncio.create_task(fib())
    task2 = asyncio.create_task(factorial())
    task3 = asyncio.create_task(sqrt())
    task4 = asyncio.create_task(cubic())

    await asyncio.gather(task1, task2, task3, task4)


if __name__ == '__main__':
    asyncio.run(main())
