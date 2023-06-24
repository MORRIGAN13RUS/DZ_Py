# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
def dz3_z1_f1(my_list):
    my_set=set()
    for i in my_list:
        n = my_list.count(i)
        if n>1:
            my_set.add(i)
    my_list_2=[ i for i in my_set]
    return my_list_2
print ( dz3_z1_f1([1, "dfff", 85, 98, "dfff", 25, 78,85,85,33,85]))

def dz3_z1_f2(my_list):
    my_set={ i for i in my_list}
    my_list2=[]
    for i in my_set:
        n = my_list.count(i)
        if n>1:
            my_list2.append(i)
    return my_list2
print ( dz3_z1_f2([1, "dfff", 85, 98, "dfff", 25, 78,85,85,33,85]))
