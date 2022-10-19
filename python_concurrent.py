# coding: utf-8
import asyncio
from concurrent import futures

import aiohttp
import requests


def req(page):
    return requests.get(f"http://vmaig.com/?page={page}")

def fetch_many():
    with futures.ThreadPoolExecutor(3) as executor:
        to_dos = [executor.submit(req, page) for page in range(1, 11)]
        for future in futures.as_completed(to_dos):
            print(future.result())

def fetch_many2():
    with futures.ProcessPoolExecutor(3) as executor:
        to_dos = [executor.submit(req, page) for page in range(1, 11)]
        for future in futures.as_completed(to_dos):
            print(future.result())

async def req_aio(page, sem):
    async with sem:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://vmaig.com/?page={page}") as resp:
                print(resp.status)

async def fetch_many3():
    sem = asyncio.Semaphore(3)
    await asyncio.gather(*[req_aio(page, sem) for page in range(1, 11)])


if __name__ == "__main__":
    fetch_many()
    fetch_many2()

    asyncio.run(fetch_many3())
