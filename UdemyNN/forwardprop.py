import numpy as np
import matplotlib.pyplot as plt

# Number of classes
Nclass = 500

# Gaussian cloud
cloud = np.random.randn(Nclass, 2)
X1 = cloud + np.array([0, -2])
X2 = cloud + np.array([2, 2])
X3 = cloud + np.array([-2, 2])
X = np.vstack([X1, X2, X3])

Y = np.array([0]*Nclass + [1]*Nclass + [2]*Nclass)
print(Y)

# plt.scatter(X1[:,0], X1[:,1])
# plt.scatter(X2[:,0], X2[:,1])
# plt.scatter(X3[:,0], X3[:,1])
# plt.show()

D = 2
M = 3
K = 3

W1 = np.random.randn(D, M)
b1 = np.random.randn(M)
W2 = np.random.randn(M, K)
b2 = np.random.randn(K)

def forward(X, W1, b1, W2, b2):
    Z = 1/(1 + np.exp(-X.dot(W1)-b1)) # or np.exp(np.dot(-X, W1)-b1)
    A = np.dot(Z, W2) + b2
    # The following is the softmax process (exponentiation and normalization)
    expA = np.exp(A)
    Y = expA/expA.sum(axis=1, keepdims=True)
    return Y

def classification_rate(Y, P):
    correct = 0
    total = 0
    for i in range(len(Y)):
        total += 1
        if Y[i] == P[i]:
            correct += 1
    return float(correct/total)

probY = forward(X, W1, b1, W2, b2)
P = np.argmax(probY, axis=1)

assert(len(P) == len(Y))

print('Classification rate for random weights: ', classification_rate(Y,P))