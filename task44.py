##Задача 44: В ячейке ниже представлен код генерирующий DataFrame, 
#которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сделать без встроенных ф-ций, например,get_dummies?
import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head(20)

data.loc[data['whoAmI'] == 'robot', 'robot' ] = '1'
data.loc[data['whoAmI'] == 'human', 'human' ] = '1'
data = data.fillna(0)
