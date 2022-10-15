import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

train_data = np.load('Balanced_data\watch_dogs_total_balanced_data.npy',allow_pickle=True)
df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

lefts = []
rights = []
forwards = []

shuffle(train_data)

for data in train_data:
    img = data[0]
    choice = data[1]

    if choice == [1,0,0]:
        lefts.append([img,choice])
    elif choice == [0,1,0]:
        forwards.append([img,choice])
    elif choice == [0,0,1]:
        rights.append([img,choice])
    else:
        print('!!')


print(len(lefts))
print(len(forwards))
print(len(rights))


np.save('watch_dogs_left_moves_data.npy', lefts , dtype=object)
np.save('watch_dogs_right_moves_data.npy', rights , dtype=object)
np.save('watch_dogs_forward_moves_data.npy', forwards , dtype=object)






