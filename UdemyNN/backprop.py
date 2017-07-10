import numpy as np
import matplotlib.pyplot as plt


def forward(X, W1, b1, W2, b2):
    Z = 1/(1 + np.exp(-X.dot(W1)-b1)) # or np.exp(np.dot(-X, W1)-b1)
    A = np.dot(Z, W2) + b2
    # The following is the softmax process (exponentiation and normalization)
    expA = np.exp(A)
    Y = expA/expA.sum(axis=1, keepdims=True)
    return Y, Z


def classification_rate(Y, P):
    correct = 0
    total = 0
    for i in range(len(Y)):
        total += 1
        if Y[i] == P[i]:
            correct += 1
    return float(correct/total)


# I thought there was another log term in this function
def cost(T, Y):
    tot = T*np.log(Y)
    return tot.sum()


def derivative_w2(Z, T, Y):
    # N, K = T.shape
    # M = Z.shape[1]

    # slow, non-vectorized implementation
    # ret1 = np.zeros((M, K))
    # for n in range(N):
    #     for m in range(M):
    #         for k in range(K):
                # this is directly from the definition of the derivative in notes
                # ret1[m,k] += (T[n,k] - Y[n,k])*Z[n,m]
    # print('ret1shape ', ret1.shape)
    #
    # return ret1
    #
    # fast, vectorized implementation
    # print('Tshape ', T.shape)
    # print('Yshape ', Y.shape)
    # print('Zshape ', Z.shape)
    ret2 = np.dot((T-Y).T,Z)
    # print('ret2shape ', ret2.shape)
    return ret2


def derivative_b2(T, Y):
    return (T-Y).sum(axis=0)


def derivative_w1(X, Z, T, Y, W2):
    # N, D = X.shape
    # M, K = W2.shape

    # slow
    # ret1 = np.zeros((D, M))
    # for n in range(N):
    #     for k in range(K):
    #         for m in range(M):
    #             for d in range(D):
    #                 ret1[d,m] += (T[n,k] - Y[n,k])*W2[m,k]*Z[n,m]*(1-Z[n,m])*X[n,d]
    # return ret1

    int1 = np.dot((T-Y), W2.T)
    int2 = int1*Z*(1-Z)
    int3 = np.dot(int2.T, X)
    # print(W2.shape, (T-Y).shape)
    # print(int1.shape)
    # print(Z.shape)
    # print(int2.shape)
    # print(X.shape)
    return np.sum(int3, axis=1)

    # return np.sum(np.dot((T-Y).T, W2)*Z*(1-Z))

def derivative_b1(T, Y, W2, Z):
    return ((T-Y).dot(W2.T)*Z*(1-Z)).sum(axis=0)


def main():
    # create the data
    nClass = 500
    D = 2 # input dimensionality (num features)
    M = 3 # hidden layer size
    K = 3 # output dimensionality (num of classes)

    cloud = np.random.randn(nClass, 2)
    X1 = cloud + np.array([0, -2])
    X2 = cloud + np.array([2, 2])
    X3 = cloud + np.array([-2, 2])
    X = np.vstack([X1, X2, X3])

    Y = np.array([0] * nClass + [1] * nClass + [2] * nClass)
    N = len(Y)

    # one-hot encoding of Y
    T = np.zeros((N, K))
    for i in range(N):
        T[i, Y[i]] = 1

    plt.scatter(X[:,0], X[:,1], c=Y, s=100, alpha=0.5)
    # plt.show()

    # randomly initialize the weights
    W1 = np.random.randn(D, M)
    b1 = np.random.randn(M)
    W2 = np.random.randn(M, K)
    b2 = np.random.randn(K)

    learningRate = 10e-7
    costs = []
    epochs = 100000
    for epoch in range(epochs):
        output, hidden = forward(X, W1, b1, W2, b2)
        # every 100 epochs, calculate classification rate
        if epoch % 100 == 0:
            c = cost(T, output)
            P = np.argmax(output, axis=1)
            r = classification_rate(Y, P)
            print('Cost: ', c)
            print('Classification Rate: ', r)
            costs.append(c)
        W2 += learningRate*derivative_w2(hidden, T, output)
        b2 += learningRate*derivative_b2(T, output)
        W1 += learningRate*derivative_w1(X, hidden, T, output, W2)
        b1 += learningRate*derivative_b1(T, output, W2, hidden)

    plt.plot(cost)
    plt.show()

if __name__ == main():
    main()
