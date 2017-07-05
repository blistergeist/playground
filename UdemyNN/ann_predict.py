import numpy as np
from dataprocessing import get_data

fileName = 'C:\\Users\\Morgan\\Documents\\GitHub\\machine_learning_examples\\ann_logistic_extra\\ecommerce_data.csv'
X, Y = get_data(fileName)

M = 5   # five hidden units (arbitrary/non-trivial selection)
D = X.shape[1]  # number of features
K = len(set(Y)) # number of unique values in Y
W1 = np.random.randn(D, M)
b1 = np.zeros(M)
W2 = np.random.randn(M, K)
b2 = np.zeros(K)

def softmax(a):
    return np.exp(a)/np.exp(a).sum(axis=1, keepdims=True)

def forward(X, W1, b1, W2, b2):
    Z = np.tanh(np.dot(X, W1) + b1)
    return softmax(np.dot(Z, W2) + b2)

probY = forward(X, W1, b1, W2, b2)
P = np.argmax(probY, axis=1)

def class_rate(Y, P):
    return np.mean(Y == P)

print('Score: ', class_rate(Y, P))