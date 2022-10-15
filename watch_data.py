import numpy as np
import cv2


file_name = "watch_dogs_total_training_data.npy"

training_data = list(np.load(file_name,allow_pickle=True))

for data in training_data:
    screen = data[0]
    output = data[1]
    #screen = cv2.resize(screen,(800,600))
    cv2.imshow("data",screen)
    print(output)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

