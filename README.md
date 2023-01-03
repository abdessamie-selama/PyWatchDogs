# PyWatchDogs
A self driving car in a video game using Deep Learning

the dataset : https://www.kaggle.com/datasets/abdesamieselama/watch-dogs-dataset

demonstration : https://www.youtube.com/watch?v=s8xEZ4xYpvo

01/Collecting the Data

collecting the data starting with the collecting data part, the known idea is to record the screen and keep tracking of the pressed keys of the keyboard frame by frame while playing the game,which make a data set of lists like this [frame,pressed keys], the pressed keys is also a list of integers as bellow : 
[1.0.0] stands for left, 
[0,1,0] stands for forward,
[0,0,1] stands for right,
i have collected 1.3 M samples for the dataset.

02/Ballancing Data

03/Training the Model
finally the training part : which consist of creating a simple convolutional neural network (CNN) and train the model.
