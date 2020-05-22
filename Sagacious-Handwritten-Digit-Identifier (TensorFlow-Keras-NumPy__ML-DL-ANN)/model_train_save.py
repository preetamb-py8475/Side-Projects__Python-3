from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import to_categorical
import matplotlib.pyplot as plt


# load dataset directly from 'keras' library
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# plot first 6 samples of MNIST training dataset as gray-scale image
for i in range(6):
    plt.subplot(int('23' + str(i + 1)))
    plt.imshow(x_train[1], cmap=plt.get_cmap('gray'))

# reshape format [samples][width][height][channels]
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1).astype('float32')
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1).astype('float32')

# converts a class vector (integers) to binary class matrix
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# normalize inputs
x_train = x_train / 255
x_test = x_test / 255


# define a 'CNN' Model
def create_model():
    num_classes = 10
    model = Sequential()
    model.add(Convolution2D(32, kernel_size=(3, 3), activation='relu'))
    model.add(Convolution2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


# build the Model
model = create_model()

# fit the Model
model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=10, batch_size=200, verbose=2)
print("\nThe Model has been 'trained' successfully !!!")

# save the model
model.save('model.h5')
print("\nThe Model has been 'saved' successfully !!!")

# evaluate the Model
scores = model.evaluate(x_test, y_test, verbose=0)
print("\nCNN Error: %.2f%%" % (100 - scores[1] * 100))
