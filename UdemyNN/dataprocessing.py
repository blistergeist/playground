import numpy as np
import pandas as pd

def get_data(fileName):
    df = pd.read_csv(fileName)
    data = df.as_matrix()

    X = data[:, :-1]
    Y = data[:, -1]

    # normalize numerical columns
    X[:, 1] = (X[:,1] - X[:,1].mean() / X[:,1].std())
    X[:, 2] = (X[:,2] - X[:,2].mean() / X[:,2].std())

    # categorical column (time of day)
    # here we are creating a whole new X matrix and inserting three
    # additional one-hot encoded columns into the space where the single
    # categorical column used to be
    # HINT: the time of day column is second to last (i.e. D-1)
    # HINT: since the last column was stripped out and used as our Y,
    # we can just append whatever one-hot encoded matrix we create onto X
    N, D = X.shape
    X2 = np.zeros((N, D+3))
    X2[:, 0:(D-1)] = X[:, 0:(D-1)]

    for n in range(N):
        t = int(X[n, D-1])
        X2[n,t+D-1] = 1

    # create a matrix of zeros
    Xinsert = np.zeros((N, 4))
    # iterate through the time_of_day column and set
    # the column corresponding to time_of_day value to 1
    i = 0
    for x in X[:,(D-1)]:
        Xinsert[i,int(x)] = 1
        i += 1

    # create a matrix of zeros
    Xinsert2 = np.zeros((N,4))
    # set the column corresponding to number in the the time_of_day column to 1
    Xinsert2[np.arange(N), X[:,D-1].astype(np.int32)] = 1

    # using either of the last two methods
    return np.append(X[:,:-1],Xinsert, axis=1), Y

# this is just limiting the data to two classes
# Not sure why we are doing this
# Maybe just eliminating two classes we don't care about.
def get_binary_data(fileName):
    X, Y = get_data(fileName)
    X2 = X[Y <= 1]
    Y2 = Y[Y <= 1]
    return X2, Y2

# fileName = 'C:\\Users\\Morgan\\Documents\\GitHub\\machine_learning_examples\\ann_logistic_extra\\ecommerce_data.csv'
# # X, Y = get_data(fileName)
# X, Y = get_binary_data(fileName)
# print(X.shape)