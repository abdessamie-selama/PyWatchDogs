# PyWatchDogs
a self driving car in a video game using Deep Learning

the dataset : https://www.kaggle.com/datasets/abdesamieselama/watch-dogs-dataset
demonstration : https://www.youtube.com/watch?v=s8xEZ4xYpvo

01/Collecting the Data
STARTING WITH THE COLLECTING DATA PART, THE KNOWN IDEA IS TO RECORD THE SCREEN AND KEEP TRACKING OF THE PRESSED KEYS OF THE 
KEYBOARD FRAME BY FRAME WHILE PLAYING THE GAME,WHICH MAKE A DATA SET OF LISTS LIKE THIS [FRAME,PRESSED KEYS],
THE PRESSED KEYS IS ALSO A LIST OF INTEGERS AS BELLOW :
[1.0.0] STANDS FOR LEFT
[0,1,0] STANDS FOR FORWARD
[0,0,1] STANDS FOR RIGHT
SINCE I CREATED THREE MODELS SO I HAVE COLLECTED 186000 SAMPLES FOR THE FIRST ONE, 733824 FOR THE SECOND AND ABOUT 1.3 MILLION FOR THE THIRD VERSION.

02/Ballancing Data

03/Training the Model
FINALLY THE TRAINING PART : WICH
CONSIST OF CREATING A SIMPLE CONVOLUTIONAL NEURAL NETWORK (CNN) AND FEED IT THE BALANCED
TRAINING DATA .. AGAIN IT TOOKS 13
HOURS FOR THE FIRST MODEL, 51 H FOR THE SECONDE AND 160 H FOR THE THIRD ONE.
