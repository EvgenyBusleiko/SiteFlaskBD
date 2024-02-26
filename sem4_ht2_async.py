import asyncio
import aiohttp
import time

async def main():

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
    start_time_total = time.time()
    tasks = []
    for adress in adresses:
        task = asyncio.ensure_future(download_async(adress))
        tasks.append(task)
    await asyncio.gather(*tasks)
    print(f"Downloaded all images by async in {time.time() - start_time_total:.2f} seconds")

async def download_async(adress):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(adress) as response:

            filename = adress[adress.rfind('/') + 1:]
            with open(f'./upload/{filename}', 'w') as f:
                f.write(adress)

    print(f"Downloaded {adress} in {time.time() - start_time:.2f} seconds")




if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
