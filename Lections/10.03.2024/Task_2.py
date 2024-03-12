def Sdvig(a, step):
    for i in range(0,step):
       number=a[-1]
       a.pop()
       a.insert(0,number)
    return a
#[1,2,3,4,5,6,7,8,9,10]  дано
#[10,1,2,3,4,5,6,7,8,9]  сдвиг 1
#[9,10,1,2,3,4,5,6,7,8]  сдвиг 2
#[8, 9,10,1,2,3,4,5,6,7]  сдвиг 3
list=[1,2,3,4,5,6,7,8,9,10]
k=int(input("введите шаг сдвига "))
list_new=Sdvig(list,k)
print(list_new)