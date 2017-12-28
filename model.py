import csv
import cv2
import numpy as np

lines=[]
with open('utd/data/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader :
        lines.append(line)
images = []
measurements = []
for line in lines:
    for k in range(3) :
        source_path = line[k]
        filename = source_path.split('\\')[-1]
        current_path = 'utd/data/' +filename.strip()
        #print(current_path)
        image = cv2.imread(current_path)


        if image is None:
            print("Image path incorrect: ", current_path)
            continue  # skip adding these rows in the for loop

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)   
        image = np.asarray(image)
        #image = image[70:70+65, 0:320]
        #image = cv2.resize(image, ( 320, 65), interpolation=cv2.INTER_AREA)
        #image_array = image/255.  -0.5
        measurement = float(line[3])
        if np.round(measurement,2) != 0 :
            images.append(image)
            measurements.append(measurement)
            image_flipped = np.fliplr(image)
            images.append(image_flipped)
            measurements.append(-1*measurement)



X_train = np.array(images)
print(X_train.shape)
y_train = np.array(measurements)
print(y_train.shape)



tr_classes, tr_counts = np.unique(np.round(y_train,2), return_counts=True)
print(tr_counts.size)


t = tr_classes*100
print (t)
print (tr_counts)


from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, Cropping2D, MaxPooling2D, Convolution2D, Dropout

model = Sequential()
model.add(Lambda(lambda x: x/255.0 -0.5, input_shape=(160,320,3)))
model.add(Cropping2D(cropping=((70, 25),(0,0))))
model.add(Convolution2D(24, 5, 5, subsample=(2,2),  activation="relu"))

model.add(Convolution2D(36, 5, 5, subsample=(2,2), activation="relu"))

model.add(Convolution2D(48, 5, 5,subsample=(2,2), activation="relu"))
model.add(Convolution2D(64, 3, 3, activation="relu"))
model.add(Convolution2D(64, 3, 3, activation="relu"))

model.add(Flatten())
model.add(Dense(100))
model.add(Dropout(0.5))
model.add(Dense(50))
model.add(Dropout(0.5))
model.add(Dense(10))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam')

model.fit(X_train, y_train, validation_split=0.2, shuffle=True, nb_epoch=3)

model.save('model.h5')