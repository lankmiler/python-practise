values = list(range(0, 100))
search_value = -1
i = 0

# If remove - it cause an error. Because of algorithm
values.append(search_value)

while True:
    if values[i] == search_value: break
    i += 1
print(i)