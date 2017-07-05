import numpy as np
import pandas as pd

# fileName = 'C:\\users\\morgan\\documents\\github\\machine_learning_examples\\ann_logistic_extra\\ecommerce_data.csv'
# with open(fileName, 'rb') as f:
#     var = f.read()

def sigmoid(x):
    return 1/(1+np.exp(-x))

def softmax(a):
    return np.exp(a)/np.exp(a).sum(axis=0, keepdims=True)

X = np.array([1, 2])
W1 = np.array([[1, 1],[1, 0]])
W2 = np.array([[0, 1], [1, 1]])
Z = np.tanh(np.dot(X, W1))
print(Z.shape)
print(np.dot(Z, W2).shape)
out = softmax(np.dot(Z, W2))

print(out)
# #
# # xw = np.dot(X,W.T)
# # print('xw: ', xw)
# # Z = sigmoid(np.dot(X,W.T))
# # print('Z: ', Z)
# # Y = sigmoid(np.dot(Z,V.T))
# # print('Y: ', Y)
# #
# # z = sigmoid(np.dot(X,W.T)+b)
# # y = sigmoid(np.dot(z,V.T)+c)
# # print('New z: ', z)
# # print('New y: ', y)
#
#
# # Example
# # ALL WEIGHTS ARE RANDOMLY CHOSEN TO BEGIN WITH
# X = np.array([[0, 3.5], [1, 2], [1, 0.5]])
# Y = np.array([1, 1, 0])
# # W is a matrix of weights from input to hl
# # b is an array of bias terms from input to hl
# W = np.array([[0.5, 0.1, -0.3], [0.7, -0.3, 0.2]])
# b = np.array([0.4, 0.1, 0])
# # V is an array of weights from hl to output
# # c is a scalar bias term from hl to output
# V = np.array([0.8, 0.1, -0.1])
# c = 0.2
#
# Z = np.tanh(np.dot(X,W)+b)
# print('Z: ', Z)
# output = sigmoid(np.dot(Z, V)+c)
# print('output: ', output)
#
#
# def one_hot_encoder(Yin):
#     N = len(Yin)
#     K = max(Yin) + 1
#     Yout = np.zeros((N, K))
#     for n in range(N):
#         Yout[n, Yin[n]] = 1
#     return Yout
#
# Yin = np.random.randint(5, size=8)
# print(Yin)
# Yout = one_hot_encoder(Yin)
# print(Yout)
#
# # predictionLabels = np.argmax(Yout, axis=1)
# # targetLabels = np.argmax(targetIndicator, axis=1)
# # accuracy = sum(predictionLabels == targetLabels)/N
#
# # Softmax in code
# # last activation layer in NN
# a = np.random.randn(5)
# expa = np.exp(a)
# answer = expa/expa.sum()
# print(answer.sum())
#
# A = np.random.randn(100, 5)
# expA = np.exp(A)
# ans = expA/expA.sum(axis=1, keepdims=True)
# print(ans.sum(axis=1))