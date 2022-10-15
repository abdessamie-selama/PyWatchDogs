import numpy as np
from random import shuffle

train_data = []

for i in range(120):
    if (i != 5 and i != 6 and i != 8 and i!= 14 and i != 20 and i != 26 and i != 101):
        train_data += list(np.load("watch_dogs_"+str(i)+"_training_data.npy",allow_pickle=True))
        print(i)

forwards = []
lefts = []
rights = []
print(len(train_data))
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
print(len(lefts),len(rights),len(forwards))

SIZE = min(len(lefts),len(rights),len(forwards))
print(SIZE)
lefts = lefts[:SIZE]
rights = rights[:SIZE]
forwards = forwards[:SIZE]

train_data = lefts + rights + forwards

shuffle(train_data)
print(len(train_data))

np.save('watch_dogs_total_balanced_data.npy', train_data)
