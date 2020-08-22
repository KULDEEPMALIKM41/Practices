import time
print('working...')
i = 1
while i<101:
    time.sleep(.05)
    # print('|', end='',flush=True)
    print('>', end='',flush=True)
    i += 1