class Calculator:

    def __init__(self,*args):
        self.argument = args 
        self.len_data = len(self.argument)

    def summa(self,start=0,finish=0):
        '''Метод суммы'''
        if self.test():
            if finish == 0:
                finish = self.len_data
            data = self.argument[start:finish]
            return sum(data)
        return 'Неверный тип данных'
    
    def difference(self,start=0,finish=0):
        '''Метод разности'''
        if self.test():
            if finish == 0:
                finish = self.len_data
            data = self.argument[start:finish]
            diff=data[0] - sum(data[1:])
            return diff
        return 'Неверный тип данных'
    
    def composition(self,start=0,finish=0):
        '''Метод умножения'''
        if self.test():
            result = 1
            if finish == 0:
                finish = self.len_data
            data = self.argument[start:finish]
            for i in range(len(data)):
                result = result*data[i]
            return result
        return 'Неверный тип данных'
    
    def division(self,start=0,finish=0):
        '''Метод деления'''
        if self.test():
            result_data = []
            if finish == 0:
                finish = self.len_data        
            data = self.argument[start:finish]
            len_list = len(data)
            data = map(float,data)
            result_data.extend(data)
            result = result_data[0]
            for i in range(1,len_list):
                result = result/result_data[i]
            return result
        return 'Неверный тип данных'
    
    def test(self):
        type_list= [int,float]
        for one_element in self.argument:
            if type(one_element) not in type_list: 
                return False
            return True

        
    
    



