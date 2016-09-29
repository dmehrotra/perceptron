from random import choice
from numpy import array, dot, random
from IPython import embed
import matplotlib.pyplot as plt
bias = 1
training_data = [ 
	(array([-1,-1,bias]), -1), 
	(array([-1,1,bias]), 1), 
	(array([1,-1,bias]), 1), 
	(array([1,1,bias]), 1)
]

weights = random.rand(3)
errors=[]
learning_constant = .2

def activate(sum):
  	if (sum > 0):
  		return 1
  	else:
  		return -1

def adjust(er,training_data):
	return weights + error * training_data 

for i in xrange(100):
	data, expected = choice(training_data)
	result = activate(dot(data, weights))
	error = expected - result
	errors.append(error)
	weights = adjust(error,data)

for x, _ in training_data:
	result = activate(dot(x, weights))
	print result

plt.plot( errors )
plt.show()