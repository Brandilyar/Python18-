from Banch import degree_recursion
from Banch import degree_cycle

from simple_benchmark import benchmark
import matplotlib.pyplot as plt


function = [degree_recursion,degree_cycle]
arguments ={}
for i in range(100):
    arguments['i'+str(i)]=i
arguments_name = 'natural'
aliases = {degree_recursion:'Рекурсия',degree_cycle:"Цикл"}
banch=benchmark(function,arguments,arguments_name,function_aliases=aliases)
banch.plot()
plt.show(banch)
