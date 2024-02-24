import requests
import os
import time
import asyncio
import aiohttp

async def download_async(url):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
    filename = 'asyncio_' + url.replace('https://','').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(text)
    print(f"Downloaded {url} in {time.time() -start_time:.2f} seconds")


def task1(urls: list[str]):
    start_time = time.time()

    for url in urls:
        response = requests.get(url)
        filename = 'sync_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
        with open(f'./upload,{filename}', "w", encoding='utf-8') as f:
            f.write(response.text)
        print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")
        process = Process(target=download, args=(url,start_time))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()



def task2(urls):
    start_time = time.time()
    for url in urls:
        response = requests.get(url)
        filename = 'sync_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
        with open(f'./upload,{filename}', "w", encoding='utf-8') as f:
            f.write(response.text)
        print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")

async def task3(urls):

    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download_async(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


def main():
    urls = [
        'https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        'https://mail.ru/',
        'https://www.yahoo.com/',
        'https://www.rambler.ru/',
        'https://www.wikipedia.org/',
        'https://pikabu.ru/'
    ]
    asyncio.run (task3(urls))




if __name__ == '__main__':
    main()

