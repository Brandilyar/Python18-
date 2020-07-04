import numpy as np # numpy будет нужен в основном для работы с матрицами
import scipy.special #он нам пригодится для функции активации
import matplotlib
import matplotlib.pyplot as plt
import csv
class NeuralNetwork:
    """Класс, с помощью которого можно проводить обучения методом обратного распостранения ошибки с использованием градиентного спуска"""
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
       self.iNodes = input_nodes
       self.hNodes = hidden_nodes
       self.oNodes = output_nodes
       self.lr = learning_rate
       #матрицы весовых коэфицентов связей между wih и who
       #weights inputs x hidden
       #weights hidden x outputs
       self.wih = np.random.normal(0.0, pow(self.hNodes, -0.5), (self.hNodes, self.iNodes))
       self.who = np.random.normal(0.0, pow(self.oNodes, -0.5), (self.oNodes, self.hNodes)) #10x100
       self.activation_function = lambda x:scipy.special.expit(x) #функция активации, которая изображает, что у нас есть нейроны
       self.inverse_activation_function = lambda x:scipy.special.logit(x)
    def train(self, inputs_list, targets_list):
        #преобразовать список входящих значений в двумерный массив
        inputs = np.array(inputs_list, ndmin = 2).T
        targets = np.array(targets_list, ndmin = 2).T
        hidden_inputs = np.dot(self.wih, inputs) # 100x784 * 784x1 = 100x1
        hidden_outputs = self.activation_function(hidden_inputs) #100x1
        #расчитать сигналы для скрытого слоя
        
        final_inputs = np.dot(self.who, hidden_outputs) #10x100 * 100x1
        final_outputs = self.activation_function(final_inputs) # 10x1
        
        #ошибки выходного слоя (целевое значние - фактическое значение)
        output_errors = targets - final_outputs # 10x1
        #ошибки скрытого слоя - это ошибки output_erros, которые пропорционально распределены на весовых узлах
        hidden_errors = np.dot(self.who.T, output_errors) #100x10 *10x1 = 100x1

        #обновить весовые коэфиценты для связей между скрытыми и выходными слоями
        self.who += self.lr * np.dot((output_errors * final_outputs * (1.0 - final_outputs)), np.transpose(hidden_outputs)) # 0.2 * 10x100
        self.wih += self.lr * np.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), np.transpose(inputs))


    def query(self, inputs_list):
        """ функция опроса полученных результатов"""

        inputs = np.array(inputs_list, ndmin =2).T #ndmin -  трансорформация в двумерных массив нашего списка
       
        #рассчитать входящие сигналы для скрытого слоя
        hidden_inputs = np.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
       
        #расчитать входящие сигналы для скрытого слоя
       
        final_inputs = np.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        return final_outputs
    def backquery(self, targets_list):
        #мы идем в обратную сторону, поэтому первое действие - превратить targets_list в fina-_outputs
        final_outputs = np.array(targets_list, ndmin = 2).T
        final_inputs = self.inverse_activation_function(final_outputs)

        hidden_outputs = np.dot(self.who.T, final_inputs) 
        hidden_outputs -= np.min(hidden_outputs)
        hidden_outputs /= np.max(hidden_outputs)
        hidden_outputs *= 0.98
        hidden_outputs += 0.01

        hidden_inputs = self.inverse_activation_function(hidden_outputs)
        inputs = np.dot(self.wih.T, hidden_inputs) 
        inputs -= np.min(hidden_outputs)
        inputs /= np.max(hidden_outputs)
        inputs *= 0.98
        inputs += 0.01


        return inputs


n  = NeuralNetwork(784, 300, 27, 0.2)

train_data_file = open("emnist-letters-train.csv", 'r')
train_data_list = train_data_file.readlines()
train_data_file.close()
for record in train_data_list:
    all_values = record.split(',')
    #отмасштабировать наши значения, потому что от 0 до 255 нас не устраивает, наша нейросеть работаь с этим не сможет
    inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    targets = np.zeros(27) + 0.01
    #выставим целевое значение
    targets[int(all_values[0])] = 0.99
    n.train(inputs, targets)
# запись весов в файл
with open('resultWHO.csv','a',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(n.who)
with open('resultWIH.csv','a',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(n.wih)

# Чтение весов из файл
'''with open ('resultWIH.csv','r') as file:
    wih = []
    reader = file.readlines()
    for row in reader:
        all_values = row.split(',')
        wih.append(np.asfarray(all_values))
with open ('resultWHO.csv','r') as file:
    who = []
    reader = file.readlines()
    for row in reader:
        all_values = row.split(',')
        who.append(np.asfarray(all_values))'''

test_data_file = open("emnist-letters-test.csv", "r")
test_data_list = test_data_file.readlines()
test_data_file.close()



scorecard = []
#Перебрать все наши значения в тестовом наборе данных
for record in test_data_list:
    all_values = record.split(',')
    correct_label = int(all_values[0])
    print(correct_label, "истинный маркер")
    inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    #произведем опрос сети
    outputs = n.query(inputs)
    #Какое число в ответе нейросети является большим, такое и представляет из себя правильный ответ
    label = np.argmax(outputs)
    print(label, "а сеть считает что...")
    if(label == correct_label):
        scorecard.append(1)
    else:
        scorecard.append(0)

scorecard_array = np.asarray(scorecard)
print("Эффективность нашей нейронной сети равна", scorecard_array.sum() / scorecard_array.size )


'''all_values = test_data_list[101].split(',')
print(all_values[0])
image_array = np.asfarray(all_values[1:]).reshape((28,28))
matplotlib.pyplot.imshow(image_array, cmap="Greys", Interpolation ="None")
matplotlib.pyplot.show()'''



'''label  = 3
targets = np.zeros(10) +0.01
targets[label] = 0.99

image_data = n.backquery(targets)
plt.imshow(image_data.reshape(28,28), cmap='Greys', Interpolation ="None")
plt.axis("off")
plt.show()
# kernel = np.array([[0,-1,0],
#                    [-1, 3,-1],
#                    [0, -1, 0]
#                    ])
image = cv2.imread(image_data.reshape(28,28))
plt.imshow(image, cmap="gray")
plt.axis("off")
plt.show()'''
