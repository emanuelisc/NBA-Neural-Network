import numpy as np

# # X = (team level, last 10 avarage score), y = won or lost
TrainingData = np.array(([1,2]), dtype=int)
TrainingResults = np.array(([100, 72]), dtype=int)
xTest = np.array(([1,2]), dtype=int)
xResults = np.array(([100,72]), dtype=int)

with open('allData.txt', 'r') as f:
  array = [[int(x) for x in line.split()] for line in f]
counter = 0
for i in array:
  if counter < len(array) / 10:
    xTest = np.vstack([xTest, [i[0], i[1]]])
    xResults = np.vstack([xResults, [i[2], i[3]]])
  X = np.vstack([TrainingData, [i[0], i[1]]])
  y = np.vstack([TrainingResults, [i[2], i[3]]])
  counter += 1

max = np.amax(y)
# scale units
# X = X/np.amax(X, axis=0) # maximum of X array
# xPredicted = xPredicted/np.amax(xPredicted, axis=0) # maximum of xPredicted (our input data for the prediction)
TrainingResults = TrainingResults/max # max test score is 100

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

  def predict(self):
    rightCounter = 0
    for i in range(len(xTest)):
      # print("Predicted data based on trained weights: ")
      print("Input (scaled): \n" + str(xTest[i]))
      print("ActualResults :\n" + str(xResults[i]))
      output = self.forward(xTest[i])
      print("Output: \n" + str(output))
      if output[0] > output[1] and xResults[i][0] < xResults[i][1]:
        rightCounter += 1
      elif output[0] < output[1] and xResults[i][0] > xResults[i][1]:
        rightCounter += 1
    print("Accuracy: " + str(rightCounter / len(xTest)))



def trainNetwork():
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
  NN.predict()

# trainNetwork()
