import time
start = time.time()

values = range(0, 100)
search_value = 56
i = 0

while True:
    if i < len(values):
        if values[i] == search_value:
            end = time.time()
            print('Found')
            break
    i += 1
