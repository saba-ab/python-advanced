from threading import Thread


def print_nums():
    for i in range(1, 6):
        print(i)


thread = Thread(target=print_nums)

thread.start()
thread.join()
