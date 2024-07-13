def swap_elements(list, order1, order2):
    temp=list[order1]
    list[order1]=list[order2]
    list[order2]=temp
    return list

List = [43, 15, 59, 99]
order1, order2 = 1, 3
 
print(swap_elements(List, order1-1, order2-1))

