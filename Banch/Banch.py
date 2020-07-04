count = 0
def degree_recursion(degree,result_list=[]):
    global count
    count = count + 1
    number = 5
    if degree == 0 or degree == 1:
        return 1
    else:
        result = number * degree_recursion(degree-1,result_list)
        result_list.append(result)
        '''if degree == count:
            return result_list
        else:'''
        return result

def degree_cycle(degree):
    result = []
    number = 5
    if degree == 0 or degree == 1:
        return 1 
    else:
        for i in range(1,degree):
            result=number**i
    return result
