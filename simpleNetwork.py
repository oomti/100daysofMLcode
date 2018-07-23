import numpy as np

inputArray = [0 for x in range(3) ]
hiddenLayer = [0 for x in range(4) ]
outputArray = [0 for x in range(3) ]

deltaInputArray
deltaHiddenLayer = [0 for x in range(4) ]
deltaOutputArray = [0 for x in range(3) ]

weightTensorInput = [[0 for x in range(3)] for y in range(4)]  
weightTensorOutput = [[0 for x in range(4)] for y in range(3)]

#The weight tensor values only depend on the previous neuron
deltaWeightTensorInput = [[0 for x in range(3)] for y in range(4)]  
deltaWeightTensorOutput = [[0 for x in range(4)] for y in range(3)]

biasInput = [0 for x in range(4) ]

targetVector = [0 for x in range(3) ]
errorVector = [0 for x in range(3) ]
deltaErrorVector = [0 for x in range(3) ]
arrayOfOnes = [0 for x in range(3) ]


eta=0.4

#This function does one whole loop the the given neural network
def iterate()
	#Update inputs
	#Feed hidden layer
	forward(inputArray, hiddenLayer, weightTensorInput, biasInput)
	#Feed output layer
	forward(hiddenLayer, outputArray, weightTensorOutput, biasOutput)
	#Have to create the error and it`s partial derivative at the output layer, to feed it backwards
	errorMeasure(targetVector, errorVector, outputArray, deltaErrorVector)
	#Update last weight tensor
	backward(hiddenLayer, outputArray, weightTensorOutput, deltaOutputArray, deltaHiddenLayer, deltaWeightTensorOutput, deltaErrorVector)
	#Update first weight tensor
	backward(inputArray, hiddenLayer, deltaWeightTensorInput, deltaHiddenLayer, deltaInputArray, deltaWeightTensorInput, arrayOfOnes)




def errorMeasure(targetVector, errorVector, outputLayer, deltaErrorVector)
	for indexTarget, valueTarget in enumerate(outputLayer):
		errorVector[indexTarget]=1/2 * (targetVector[indexTarget]-outputLayer[indexTarget])^2
		deltaErrorVector[indexTarget] = (outputLayer[indexTarget] - targetVector[indexTarget] ) / 3



#Feedforward function: 

#add bias, sum previous inputs*weights, activate

def forward(inputLayer, outputLayer ,weightTensor, bias):
	for indexTarget, valueTarget in enumerate(outputLayer):
		#add bias
		outputLayer[indexTarget] = bias[indexTarget]
		for indexInput, valueInput in enumerate(inputLayer):
		#sum previous neuron signals*weights
			outputLayer[indexTarget] += weightTensor[indexTarget][indexInput]*inputLayer[indexInput]
		#activate
		outputLayer[indexTarget] = activate(outputLayer[indexTarget])

	return outputLayer

#Backpropagation function, going from "right to left"
def backward(inputLayer, outputLayer,weightTensor, deltaOutputLayer, deltaInputLayer, deltaWeightTensor, errorValue):
	for indexTarget, valueTarget in enumerate(outputLayer):
		# setting the nodes derivative from the previous error and the derivative of the activation function
		deltaOutputLayer[indexTarget] = errorValue[indexTarget]*activate(outputLayer[indexTarget],True)
		#InputLayer neurons set to zero for summing up.
		deltaInputLayer[indexTarget] = 0

		for indexInput, valueInput in enumerate(inputLayer):
			#Calculating each element of the derivative on the weight tensor
			deltaWeightTensor[indexTarget][indexInput] = deltaOutputLayer[indexTarget] * inputLayer[indexInput]
			#Setting the new value for the weight tensor
			weightTensor[indexTarget][indexInput] = weightTensor[indexTarget][indexInput] - eta * deltaWeightTensor[indexTarget][indexInput]
			#Summing up the changes on the input neuron, to propagate further
			deltaInputLayer[indexTarget] += deltaWeightTensor[indexTarget][indexInput]


#Using sigmoid function as activation, even though it`s old and not efficient method, only for practical reasons
def activate(x,deriv=False):	
	if(deriv == True):
		return x * (1 - x)
	return 1 / (1 + np.exp( - x))

