# 0x02. Python - Async Comprehension

## Python’s async comprehensions are a powerful feature introduced in Python 3.6. They allow for the creation of asynchronous lists, sets, and dictionaries using a concise syntax, similar to synchronous comprehensions.

Here’s a step-by-step guide on how to use them:

Make sure you’re using Python 3.6 or a later version, as this feature was introduced in Python 3.6.
Asynchronous comprehensions are only allowed inside an async def function. So, your function needs to be defined as async def to use async comprehensions.
Here’s a basic example of an async comprehension creating an asynchronous list:
import asyncio

async def fetch_data(url):
    ...

async def main():
    urls = [
        'http://python.org',
        'http://web.archive.org',
        'http://github.com',
    ]
    results = await asyncio.gather(*[fetch_data(url) for url in urls])
    print(results)

if __name__ == '__main__':
    asyncio.run(main())

In this example, fetch_data is a placeholder for an asynchronous operation, such as fetching data from a URL using aiohttp. The async comprehension [fetch_data(url) for url in urls] creates a list of coroutines. The asyncio.gather(*coroutines) function then runs all these coroutines concurrently and returns a list of the results.

Similarly, you can use async comprehensions for sets and dictionaries:
async def fetch_data(url):
    ...

async def main():
    urls = [
        'http://python.org',
        'http://web.archive.org',
        'http://github.com',
    ]

    # asynchronous set comprehension
    async_set = {fetch_data(url) async for url in urls}
    print(async_set)

    # asynchronous dictionary comprehension
    async_dict = {url: fetch_data(url) async for url in urls}
    print(async_dict)

if __name__ == '__main__':
    asyncio.run(main())

In the asynchronous set comprehension, each coroutine is added to the set as soon as it’s finished. In the asynchronous dictionary comprehension, the URL is used as the key and the result of the coroutine as the value.

Remember, async comprehensions are just a syntactic sugar for creating lists, sets, and dictionaries of coroutines. They don’t change the fundamental behavior of asynchronous code; they just make it easier to write.
