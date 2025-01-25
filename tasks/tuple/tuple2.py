random_numbers_list = []
for i in range(0,10):
    random_numbers_list.append(i+1)

random_numbers_tuple = tuple(random_numbers_list)

for i in range(1, len(random_numbers_tuple)):
    if i % 2 !=0:
     print(i, end=' ')
