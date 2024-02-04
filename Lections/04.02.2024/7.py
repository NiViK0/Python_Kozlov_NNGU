numbers = [1, 2, 3, 4, 5, 6]
def filter_odd_num(in_num, min, max):
    if in_num>min or in_num<=max: 
        min=int(input("Введите минимальное значние:"))
        max=int(input("Введите максимальное значение:"))
        if in_num>=min or in_num<=max:
            return True 
    else:
        return False
out_filter = filter(filter_odd_num(3, 9), numbers)

print("Тип объекта out filter:", type(out_filter))