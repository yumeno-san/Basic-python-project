def input_toll() :
    # receiving the toll of number which we want to sort
    global x
    try :
        x = int(input('how many number you want to enter ? '))

    except :

        print('please give me integer, not something else')
        input_toll()


def receiving_integer() :
    # receiving numbers which we want to sort
    input_toll()
    global list1
    list1 = []
    y = 0
    while y != x :
        try :
            v = int(input('enter the number which you want to sort :'))
            list1.append(v)
            y += 1
            

        except :
            print('please give me integer number, not something else')
            print('try again!!!!!')
                    
            
            

def sorting_list_numbers() :
    # choosing the min of list1 and add it to list2 also remove it from list1 and repetition this act until list1 get empty
    
    receiving_integer()
    list2 = []
    for a in range(len(list1)) :
        list2.append(min(list1))
        list1.remove(min(list1))
    print(list2)


sorting_list_numbers()