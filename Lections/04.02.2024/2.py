list_of_month_template = ['January', 'February', 'March', 'April' , 'May', 'June', 'July', 'August' ]
list_of_month = ['March', 'August', 'January', 'April']
list_res=[]
for iter in list_of_month_template:
    if iter in list_of_month:
        list_res.append(iter)
print(list_res)