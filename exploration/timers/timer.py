import time


def countdown(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n = n - 1
        if n == 0:
            print('BLAST OFF!!')


countdown(50)
