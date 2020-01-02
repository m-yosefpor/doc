import tensorflow as tf

Y = keras.utils.to_categrical(y)

model = tf.keras.models.Sequential()

model.add( tf.keras.layers.Flatten( input_shape=(m,n) ) )

tf.keras.layers.Conv2D( (28,28) , ....)

tf.keras.layers.Dense(12 , activation='relu', input_dim=32)
tf.keras.layers.Dropout(0.2)
tf.keras.layers.Dense(10 , activation='relu')
tf.keras.layers.Dropout(0.2)

tf.keras.layers.Dense(5 , activation='softmax') #softmax >1
tf.keras.layers.Dense(1 , activation='sigmoid') # sigmoid ==1

model.compile( 'adam' , 'binary_crossentropy' or 'categorical_crossentropy' , ...  )



model.fit(X_train, Y_train , batch_size , epochs=1 , verbose=1 , callbacks=[early , check] use_multiprocessing=True , workers =1)

model.evaluate(X_test,Y_test)

model.predict(X)
