current_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(map(lambda x: x*2 if x%2==0 else x, current_list))
print(new_list)