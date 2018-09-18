#Importing libraries and defining the functions
%matplotlib notebook
import scipy
import matplotlib as mpl
import numpy as np
import random

arraysize = 500
Participants = np.ones((arraysize))*100 + np.random.rand((arraysize))/100

def tradeValue(participant_A, participant_B):
    return min(participant_A, participant_B)

def exchangeFactor():
    return (random.random()-1/2)*0.3

def tradeSkew(participant_A, participant_B):
    valueRatio = np.abs(participant_A - participant_B) / (np.abs(participant_A - participant_B)+1)
    skewedRatio = valueRatio*0.2*np.sign(participant_A - participant_B)
    return random.random()-0.5+skewedRatio
    

def evolutionStep(participants):
    indexA = random.randint(0,len(participants)-1)
    indexB = random.randint(0,len(participants)-1)
    exchangeValue = tradeValue(participants[indexA], participants[indexB]) * \
        exchangeFactor() * tradeSkew(participants[indexA], participants[indexB])
    participants[indexA] += exchangeValue
    participants[indexB] -= exchangeValue
    return exchangeValue

def simulate(arraysize=15000, stepnumber=100000):
    tradeHistory=[]
    Participants = np.ones((arraysize))*100 + np.random.rand((arraysize))/10000
    for i in range(stepnumber):
        tradeValue=(evolutionStep(Participants))
        
    return ( Participants , tradeHistory )
