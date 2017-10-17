import time


def count_down():
    # start with 1 minutes --> 60 seconds
    for t in range(60, -1, -1):
        # format as 2 digit integers, fills with zero to the left
        # divmod() gives minutes, seconds
        sf = "{:02d}:{:02d}".format(*divmod(t, 60))
        # print(sf)  # test
        # time_str.set(sf)
        # root.update()
        # delay one second
        print(sf)
        time.sleep(1)


count_down()

