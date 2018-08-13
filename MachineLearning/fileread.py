import tensorflow as tf
import csv
import numpy as np
#import gradient_descent as gd
from tensorflow.python.training import optimizer
from tensorflow.python.training import gradient_descent

i = 1
num_rows = 9
y_actual = []
a = np.zeros((14999,), dtype=np.float32)
nvd = np.array([a])
with open('HR_comma_sep.csv') as csvfile:
	readr = csv.reader(csvfile, delimiter=',')
	for row in readr:
		if(i<num_rows):
 			x = np.array(row)
 			y = x.astype(np.float32)
 			nvd = np.concatenate((nvd, [y.tolist()]), axis=0)
 			i=i+1
		elif(i==num_rows):
 			x = np.array(row)
 			y = x.astype(np.float32)
 			y_actual = y.tolist()
#print(nvd)
print("Y_actual = ")
#print(y_actual)
features = tf.stack(nvd)
print("feature tensor = ")
print(features)
with tf.Session() as sess:
  tf.global_variables_initializer().run()
  coord = tf.train.Coordinator()
  threads = tf.train.start_queue_runners(coord=coord)
  for j in range(num_rows):
    # Retrieve a single instance:
  	example = sess.run([features[j]])
  	print(example)
  coord.request_stop()
  coord.join(threads)

W = np.ones((1,9), dtype=np.float)
W = W/490
#b = tf.Variable(1.0, dtype=np.float))
b = -0.10

y_calculated = tf.matmul(W,features)
tf.add(y_calculated,b)
print("Y_calculated = ")
s = tf.Session()
print(s.run(y_calculated))
print(y_calculated)

loss = tf.reduce_mean(tf.square(y_actual - tf.to_float(y_calculated)),axis = None, keep_dims = True)

print("Loss = ")
print(s.run(loss))
print("W is = ")
print(W)

weights = tf.Variable(W)
bias = tf.Variable(np.random.uniform(1,1000))
init = tf.global_variables_initializer()
tf.Session().run(init)
learning_rate = 0.01
step = tf.Variable(0, trainable=False)
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss, global_step = step,var_list=[bias])
#train = optimizer.minimize(loss, global_step=None, var_list=[weights], gate_gradients=optimizer.GATE_OP, aggregation_method=None, colocate_gradients_with_ops=False, name=None, grad_loss=None)
##train = optimizer.minimize(loss)
init = tf.initialize_all_variables()

s1 = tf.Session()
s1.run(init)

for step in xrange(201):
	s1.run(train)
	if step%20 == 0:
		print(step, s1.run(W), s1.run(b))


