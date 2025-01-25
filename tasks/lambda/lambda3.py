start_list = [10, 15, 20, 25, 30, 31]
result = list(filter(lambda x:(x % 5 == 0), start_list))
print(result)