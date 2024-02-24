import multiprocessing
import time


def worker(num):
    print(f"Запущен процеес {num}")
    time.sleep(3)
    print(f"Завершен процеес {num}")


if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)

    for p in processes:
        p.start()
        p.join()

    print(f"Все процессы завершили работу")
