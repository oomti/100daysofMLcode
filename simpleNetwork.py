import numpy as np
import matplotlib as mpl

inputLayer = np.zeros(3)
hiddenLayer = np.zeros(4)
outputLayer = np.zeros(3)

deltaInputLayer = np.zeros(3)
deltaHiddenLayer = np.zeros(4)
deltaOutputLayer = np.zeros(3)


np.random.seed(15)
weightTensorInput = np.random.rand(4,3) 
weightTensorOutput = np.random.rand(3,4) 

#The weight tensor values only depend on the previous neuron by computation
deltaWeightTensorInput = np.zeros((4,3))
deltaWeightTensorOutput = np.zeros((3,4))

biasInput = np.zeros(4)
biasHidden = np.zeros(4)
biasOutput = np.zeros(4)

targetArray = np.zeros(3)
errorArray = np.zeros(3)
deltaErrorArray = np.zeros(3)
layerOfOnes = np.ones(3)

eta=0.4
error=[]


def plotError():
	mpl.pyplot.imshow(image)
	


def train():
	for i in range(0,10000):
		j=np.random.randint(0,1500)
		iterate(inputs[j],target[j])
		error.append(sum(errorArray)/3)
		scanNetwork(image, xArray, yArray)
		plotError()
		



def scanNetwork(image, xArray, yArray):
	for x_index, x in range(xArray):
		for y_index, y in range(yArray):
			testNetwork((x , y , 0))
			image[x_index, y_index , 0]=outputLayer[0]
			image[x_index, y_index , 1]=outputLayer[1]
			image[x_index, y_index , 2]=outputLayer[2]



#This function does one whole loop the given neural network, during training
def trainNetwork(inputLayer,targetArray):
	#Update inputs
	#Feed hidden layer
	forward(inputLayer, hiddenLayer, weightTensorInput, biasInput)
	#Feed output layer
	forward(hiddenLayer, outputLayer, weightTensorOutput, biasOutput)
	#Have to create the error and it`s partial derivative at the output layer, to feed it backwards
	errorMeasure(targetArray, errorArray, outputLayer, deltaErrorArray)
	#Update last weight tensor
	backward(hiddenLayer, outputLayer, weightTensorOutput, deltaOutputLayer, deltaHiddenLayer, deltaWeightTensorOutput, deltaErrorArray)
	#Update first weight tensor
	backward(inputLayer, hiddenLayer, deltaWeightTensorInput, deltaHiddenLayer, deltaInputLayer, deltaWeightTensorInput, layerOfOnes)

def testNetwork(inputLayer):
	#Update inputs
	#Feed hidden layer
	forward(inputLayer, hiddenLayer, weightTensorInput, biasInput)
	#Feed output layer
	forward(hiddenLayer, outputLayer, weightTensorOutput, biasOutput)
	#Have to create the error and it`s partial derivative at the output layer, to feed it backwards
	#errorMeasure(targetArray, errorArray, outputLayer, deltaErrorArray)





def errorMeasure(targetArray, errorArray, outputLayer, deltaErrorArray):
	for indexTarget, valueTarget in enumerate(outputLayer):
		errorArray[indexTarget]=1/2 * (targetArray[indexTarget]-outputLayer[indexTarget]) ** 2
		deltaErrorArray[indexTarget] = (outputLayer[indexTarget] - targetArray[indexTarget] ) / 3



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

