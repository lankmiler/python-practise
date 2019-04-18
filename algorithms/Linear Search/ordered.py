values = list(range(0, 100))
search_value = -1
i = 0
# If remove - it cause an error. Because of algorithm
values.append(search_value)
found = False

while True:
    # Can be replaced by "assert"
    if i >= len(values):
        break
    if values[i] == search_value: found = True
    i += 1
print(found)