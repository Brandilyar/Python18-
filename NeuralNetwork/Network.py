import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt


train_data_file = open("emnist-letters-train.csv", 'r')
train_data_list = train_data_file.readlines()
train_data_file.close()
data_train=[]
data_train_label=[]
for record in train_data_list:
    all_values = record.split(',')    
    inputs_data = (np.asfarray(all_values[1:]) / 255.0).reshape((28,28))
    data_train.append(inputs_data)
    data_train_label.append(int(all_values[0]))
data_ready = np.array(data_train)
label_train = np.array(data_train_label)




train_data_file = open("emnist-letters-test.csv", 'r')
train_data_list = train_data_file.readlines()
train_data_file.close()
data_test=[]
data_test_label=[]
for record in train_data_list:
    all_values = record.split(',')    
    inputs_data = (np.asfarray(all_values[1:]) / 255.0).reshape((28,28))
    data_test.append(inputs_data)
    data_test_label.append(int(all_values[0]))
data_test_ready =  np.array(data_test)
test_label = np.array(data_test_label)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(27, activation='softmax')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(data_ready, label_train, epochs=10)
test_loss, test_acc = model.evaluate(data_test_ready,  test_label, verbose=2)

print('\nТочность на проверочных данных:', test_acc)


predictions = model.predict(data_test_ready)
print('Истинное число '+str(test_label[0])+', а нейросеть считает что '+ str(np.argmax(predictions[0])))
