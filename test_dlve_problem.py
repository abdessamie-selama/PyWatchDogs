import numpy as np


train_data = np.load('watch_dogs_2_training_data.npy',allow_pickle=True)

lefts = []
rights = []
forwards = []


for data in train_data:
    img = data[0]
    choice = data[1]
    print(choice)
    if choice == [1,0,0]:
        lefts.append([img,choice])
    elif choice == [0,1,0]:
        forwards.append([img,choice])
    elif choice == [0,0,1]:
        rights.append([img,choice])
    else:
        print('no matches')

print(len(rights))
print(len(lefts))
print(len(forwards))
