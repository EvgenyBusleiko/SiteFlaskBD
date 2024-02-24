import requests
import os
import time


def task1(urls: list[str]):
    start_time = time.time()
    threads =[]

    for url in urls:
        response = requests.get(url)
        filename = 'sync_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(f'./upload,{filename}', "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


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



if __name__ == '__main__':
    main()
