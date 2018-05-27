import numpy as np

# X = (team level, last 10 avarage score), y = won or lost
X = np.array(([1,2], [1, 3], [2, 3], [1, 2], [2,3]), dtype=int)
y = np.array(([100, 52], [89, 85], [58, 89], [58,45], [78,87]), dtype=int)
xPredicted1 = np.array(([1,3]), dtype=int)
xResult1 = np.array(([89,85]), dtype=int)
# 1 9 104 115
xPredicted2 = np.array(([1,9]), dtype=int)
xResult2 = np.array(([104,115]), dtype=int)
# 1 8 90 110
xPredicted3 = np.array(([1,8]), dtype=int)
xResult3 = np.array(([90,110]), dtype=int)
# 1 16 93 93
xPredicted4 = np.array(([1,16]), dtype=int)
xResult4 = np.array(([93,93]), dtype=int)
# 1 23 93 113
xPredicted5 = np.array(([1,23]), dtype=int)
xResult5 = np.array(([93,113]), dtype=int)
# 1 7 93 98
xPredicted6 = np.array(([1,7]), dtype=int)
xResult6 = np.array(([93,98]), dtype=int)
# 1 6 100 121
xPredicted7 = np.array(([1,6]), dtype=int)
xResult7 = np.array(([100,121]), dtype=int)
# 1 30 83 108
xPredicted8 = np.array(([1,30]), dtype=int)
xResult8 = np.array(([83,108]), dtype=int)

with open('scores.txt', 'r') as f:
  array = [[int(x) for x in line.split()] for line in f]

for i in array:
  X = np.vstack([X, [i[0], i[1]]])

  y = np.vstack([y, [i[2], i[3]]])

max = np.amax(y)
# scale units
# X = X/np.amax(X, axis=0) # maximum of X array
# xPredicted = xPredicted/np.amax(xPredicted, axis=0) # maximum of xPredicted (our input data for the prediction)
y = y/max # max test score is 100

# PRINT TEAMS
# print(X)
# PRINT SCORES
# print(y)

class Neural_Network(object):
  def __init__(self):
    #parameters
    self.inputSize = 2
    self.outputSize = 2
    self.hiddenSize = 3

    #weights
    self.W1 = np.random.randn(self.inputSize, self.hiddenSize) # (3x2) weight matrix from input to hidden layer
    self.W2 = np.random.randn(self.hiddenSize, self.outputSize) # (3x1) weight matrix from hidden to output layer

  def forward(self, X):
    #forward propagation through our network
    self.z = np.dot(X, self.W1) # dot product of X (input) and first set of 3x2 weights
    self.z2 = self.sigmoid(self.z) # activation function
    self.z3 = np.dot(self.z2, self.W2) # dot product of hidden layer (z2) and second set of 3x1 weights
    o = self.sigmoid(self.z3) # final activation function
    return o

  def sigmoid(self, s):
    # activation function
    return 1/(1+np.exp(-s))

  def sigmoidPrime(self, s):
    #derivative of sigmoid
    return s * (1 - s)

  def backward(self, X, y, o):
    # backward propgate through the network
    self.o_error = y - o # error in output
    self.o_delta = self.o_error*self.sigmoidPrime(o) # applying derivative of sigmoid to error

    self.z2_error = self.o_delta.dot(self.W2.T) # z2 error: how much our hidden layer weights contributed to output error
    self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2) # applying derivative of sigmoid to z2 error

    self.W1 += X.T.dot(self.z2_delta) # adjusting first set (input --> hidden) weights
    self.W2 += self.z2.T.dot(self.o_delta) # adjusting second set (hidden --> output) weights

  def train(self, X, y):
    o = self.forward(X)
    self.backward(X, y, o)

  def saveWeights(self):
    np.savetxt("w1.txt", self.W1, fmt="%s")
    np.savetxt("w2.txt", self.W2, fmt="%s")

  def predict(self, prediction, result):
    print (str(prediction))
    print(str(result))
    output = self.forward(prediction)
    print (str([output[0] * max, output[1] * max]))

NN = Neural_Network()
for i in range(1000): # trains the NN 1,000 times
  # print ("# " + str(i) + "\n")
  # print ("Input (scaled): \n" + str(X))
  # print ("Actual Output: \n" + str(y))
  # print ("Predicted Output: \n" + str(NN.forward(X)))
  # print ("Loss: \n" + str(np.mean(np.square(y - NN.forward(X))))) # mean sum squared loss
  # print ("\n")
  NN.train(X, y)

NN.saveWeights()
# NN.predict(xPredicted1, xResult1)
# NN.predict(xPredicted2, xResult2)
# NN.predict(xPredicted3, xResult3)
# NN.predict(xPredicted4, xResult4)
# NN.predict(xPredicted5, xResult5)
# NN.predict(xPredicted6, xResult6)
# NN.predict(xPredicted7, xResult7)
NN.predict(xPredicted8, xResult8)

