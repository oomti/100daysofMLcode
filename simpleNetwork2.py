import numpy as np
import matplotlib as mpl

class Layer:
	learningRate=0.4
	def __init__(self,inputSize, outputSize, randomSeed):
		self.neurons=np.zeros(outputSize)
		self.weights=np.random.rand(outputSize, inputSize)
		self.deltaWeights=np.zeros((outputSize, inputSize))
		self.deltaNeurons=np.zeros(outputSize)
		self.bias=np.zeros(outputSize)

	def sum(self,inputVector):
		self.neurons=np.matmul(self.weights, inputVector)+self.bias
		self.neurons=self.activate()


	def activate(self,deriv=False):
		if (deriv==True):
			return np.multiply(self.neurons,(1-self.neurons))
		return np.divide(1,(1+np.exp(-self.neurons)))


	def backpropagate(self,inputVector, errorVector):
		self.deltaNeurons=np.multiply(errorVector, self.activate(deriv=True))
		self.deltaWeights=np.outer(self.deltaNeurons, inputVector)
		self.weights-=self.learningRate*self.deltaWeights

	def get_weights(self):
		return self.weights

	def get_neurons(self):
		return self.neurons

	def get_bias(self):
		return self.bias


class Network:
	def __init__(self, layers):
		self.inputVector=np.zeros(layers[0])
		self.depth=len(layers)
		self.network=[]
		for index, size in enumerate(layers):
			if index==0:
				self.network.append(Layer(0,size,15))
			else:
				self.network.append(Layer(layers[index-1],size,15))

	def forwardPropagate(self, inputVector):
		self.inputVector=inputVector
		for index, layer in enumerate(self.network):
			if index==0:
				self.network[0].neurons=inputVector
			else:
				self.network[index].sum(self.network[index-1].neurons)


		

	def backwardPropagate(self, targetVector):
		for index, layer in reversed(list(enumerate(self.network))):
			if index==self.depth-1:
				self.network[index].backpropagate(self.network[index-1].neurons, self.error(targetVector))
			elif index==0:
				errorVector=np.sum( self.network[index+1].deltaWeights*self.network[index+1].weights , 1 )
				self.network[index].backpropagate(self.inputVector, errorVector)
			else:
				errorVector=np.sum( self.network[index+1].deltaWeights*self.network[index+1].weights , 1 )
				self.network[index].backpropagate(self.network[index-1].neurons, errorVector)

	def error(self, targetVector):
		return targetVector-self.network[self.depth-1].neurons

	def get_Weights(self, layer, )
		return self.network[layer].get_weights()



