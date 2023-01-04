import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Flatten

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "data",
    validation_split=0.2,
    subset="training",
    seed=123,
    label_mode='categorical',
    image_size=(256, 256),
    batch_size=32)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "data",
    validation_split=0.2,
    subset="validation",
    seed=123,
    label_mode='categorical',
    image_size=(256, 256),
    batch_size=32)


resnet_model = Sequential()

pretrained_model = tf.keras.applications.ResNet50(include_top=False,
                                                  input_shape=(256, 256, 3),
                                                  pooling='avg', classes=50,
                                                  weights='imagenet')
for layer in pretrained_model.layers:
    layer.trainable = False

resnet_model.add(pretrained_model)
resnet_model.add(Flatten())
resnet_model.add(Dense(1024, activation='relu'))
resnet_model.add(Dense(50, activation='softmax'))
resnet_model.summary()

my_callbacks = [
    tf.keras.callbacks.EarlyStopping(patience=2),
    tf.keras.callbacks.ModelCheckpoint(filepath='model.{epoch:02d}-{val_loss:.2f}.h5'),
    tf.keras.callbacks.TensorBoard(log_dir='./logs'),
]

resnet_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
history = resnet_model.fit(train_ds, validation_data=val_ds, epochs=50, callbacks=my_callbacks)
resnet_model.save('first_model')