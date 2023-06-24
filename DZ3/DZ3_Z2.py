# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# за основу возьмите любую статью из википедии или из документации к языку

s="Корова дает, корова не дает, корова дура. Дура она корова! Она как полная дура вообще? Остальные коровы тоже не очень умные. Они дуры, как и эта корова"
def dz3_z2_f1(big_text):
    p_list=[",",".",";",":","?","!","(",")", "[","]"]
    for i in p_list:
        n=big_text.find(i)
        if n>0:
            big_text = big_text.replace(i, '')
    big_text = big_text.lower()
    my_list = big_text.split(' ')
    return my_list    


def dz3_z2_f2(my_list):
    my_set={ i for i in my_list}
    my_dict = dict() 
    for i in my_set:
        n = my_list.count(i)
        my_dict[i] = n
    return my_dict
my_dict = dz3_z2_f2(dz3_z2_f1(s))
sorted_list = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
for i in range (10):
    print (sorted_list [i])
