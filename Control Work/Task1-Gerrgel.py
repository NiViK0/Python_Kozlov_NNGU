Names = ['Иванов', 'Петров', 'Яблочкин', 'Грушин', 'Ласточкин']
Algebra = [3, 4, 5, 5, 4]
Phisic = [2, 4, 4, 5, 3]
Russian = [2, 5, 5, 5, 2]
#mark=[[3,2,2],[4,4,5],[5,4,5],[5,5,5],[4,3,2]]
Class = ['10a', '10b', '10a', '10b', '10v']

def FindHor(Names,Algebra,Phisic,Russian):
    FIO_List=[]
    for iter in range(len(Names)):
        if Algebra[iter]>=4 and Phisic[iter]>=4 and Russian[iter]>=4:
            FIO_List.append(Names[iter])
    
    print(FIO_List)
    #return FIO_List
    
def FindOne2(Names,Algebra,Phisic,Russian):
    FIO_List=[]
    for iter in range(len(Names)):
        if Algebra[iter]==2 and Phisic[iter]>=3 and Russian[iter]>=3:
            FIO_List.append(Names[iter])
        if Algebra[iter]>=3 and Phisic[iter]==2 and Russian[iter]>=3:
            FIO_List.append(Names[iter])
        if Algebra[iter]>=3 and Phisic[iter]>=3 and Russian[iter]==2:
            FIO_List.append(Names[iter])
    
    print(FIO_List)
    #return FIO_List
def FindMaxHorClass(Names,Algebra,Phisic,Russian,Class):
    SetClass=list(set(Class))  #[10a,10б,10в] <-- {10a,10б,10в} < - - [10a,10б,10в,10а,10в]
    List_count=[] #List_count =[0,0,0]
    for iter in range(len(SetClass)):
       List_count.append(0)
       
    for iter in range(len(Names)):
        if Algebra[iter]>=4 and Phisic[iter]>=4 and Russian[iter]>=4:
            number=SetClass.index(Class[iter])
            List_count[number]=List_count[number]+1
    
    #print(FIO_List)
    print(max(List_count))
    print(SetClass)
    print(List_count)
#-----------------------
#FindHor(Names,Algebra,Phisic,Russian)
#FindOne2(Names,Algebra,Phisic,Russian)
FindMaxHorClass(Names,Algebra,Phisic,Russian,Class)
