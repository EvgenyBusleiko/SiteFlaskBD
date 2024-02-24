import requests
import os
from pathlib import Path
import time

def count_words(file):
    with open(file,encoding='utf-8') as f:
        text=f.read
        print(f'In file {file} {len(text.split())} words')


def task4():
    files =[file for files in Path.cwd() if file.is_file()]
    start_time=time.time()
    thread=[]
    for file in file:
        thread = threading.Thread(target=count_words, args=[file])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()





if __name__ == '__main__':
    task4()

