import requests
import os
import time
import  threading
import multiprocessing
import asyncio
import aiohttp



def main():

    adresses  = [
        'https://abc-decor.com/img/gallery/12/thumbs/thumb_l_PL35698.jpg',
        'https://proprikol.ru/wp-content/uploads/2020/08/krasivye-kartinki-kotikov-57.jpg',
        'https://img.razrisyika.ru/kart/99/395723-milaya-koshka-19.jpg',
        'http://mobimg.b-cdn.net/v3/fetch/3c/3cccd3c65e2abc4d5085221f2e38544c.jpeg',
        'https://s1.1zoom.ru/big3/693/Cats_Kittens_Ginger_438018.jpg',
        'https://sport-dog.ru/wp-content/uploads/4/0/a/40ab6499f014befe9b40f6402d2110c3.jpeg',
        'https://petstime.ru/wp-content/uploads/2023/04/word-image-13637-112.jpeg',
        'https://celes.club/uploads/posts/2022-10/1666949350_14-celes-club-p-kot-i-kapibara-krasivo-15.jpg',
        'https://pofoto.club/uploads/posts/2022-09/1662436552_61-pofoto-club-p-kapibara-belaya-72.jpg',
        'https://www.rabstol.net/uploads/gallery/main/497/rabstol_net_capybara_03.jpg'
    ]

    # adresses.append(input("Введите адрес для скачивания изображения: "))
    streams(adresses)

    multiproces(adresses)




def new_name(adress: str):
    start_time = time.time()
    response = requests.get(adress)
    filename = adress[adress.rfind('/')+1:]
    # print(filename)
    with open(f'./upload/{filename}', 'w') as f:
        f.write(adress)

        print(f"Downloaded {adress} in {time.time() - start_time:.2f} seconds")





def streams(adresses: list[str]):


    start_time_total = time.time()

    threads = []

    for adress in adresses:
        t = threading.Thread(target=new_name(adress))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    print(f"Downloaded all images by streams in {time.time() - start_time_total:.2f} seconds")

def multiproces(adresses: list[str]):
    processes = []
    start_time_total = time.time()


    for adress in adresses:
        p = multiprocessing.Process(target=new_name(adress))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

    print(f"Downloaded all images by multiprocessing in {time.time() - start_time_total:.2f} seconds")




# def task1(urls: list[str]):
#     start_time = time.time()
#     threads =[]
#
#     for url in urls:
#         response = requests.get(url)
#         filename = 'sync_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
#     with open(f'./upload,{filename}', "w", encoding='utf-8') as f:
#         f.write(response.text)
#     print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")

if __name__ == '__main__':
    main()
