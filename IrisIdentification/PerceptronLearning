import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

df = pd.read_csv("iris.data") # Create the Dataframe from our Dataset


y = df.iloc[0:100, 4].values # Actual description of Flower
y = np.where(y == 'Iris-setosa', -1, 1) # Setting the "Setosa" Iris to -1 and all others to 1
X = df.iloc[0:100, [0, 2]].values # Grabbing the petal length and sepal length for each Iris

'''
Below will graph a scatterplot of the petal/sepal length. Notice in the graph, there will be a distinction between
the two different Iris's. This distinction is pivotal to the Perceptron Algorithm as we can create a linear difference
between the two flowers. If this distinction was not there, without setting a set number of epochs, the program would
have a very difficult time deciphering a set difference.
'''

plt.scatter(X[:49, 0], X[:49, 1], color='red', marker='o', label='setosa')
plt.scatter(X[49:100, 0], X[49:100, 1], color='blue', marker='x', label='versicolor')
plt.xlabel('petal length')
plt.ylabel('sepal length')
plt.legend(loc='upper left')
plt.show()

'''
Below is where we create the Perceptron Algorithm.

Weight changes are based off each input.

'''

class Perceptron(object):

    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta #learning rate, default to .01
        self.n_iter = n_iter # Number of iterations over the dataset, default to 10

    def fit(self, X, y):

        '''
        Parameters:

            X : {Array-like}, shape = [n_samples, n_features] (Training vectors, where n_samples is the number of
            samples and n_features is the number of features)

            y: {Array-like}, shape = [n_samples] (Target Values)

        '''

        self.weight = np.zeros(1 + X.shape[1]) #Initialize (Array-Like structure) our weight to 0 for both lengths
        self.errorsList = [] # initialize the number of misclassifications

        for _ in range(self.n_iter):

            errors = 0
            for xi, target in zip(X, y): # iterate over the tuple for all datasets
                update = self.eta * (target - self.predict(xi)) # update != 0 if correct = prediction
                self.weight[1:] += update * xi # update !=0 and weight updated based off each length
                self.weight[0] += update # update !=0, total weight is updated
                errors += int(update != 0.0) # if update != 0, increase errors to 1

            self.errorsList.append(errors) # stores number of errors in one iteration

        return self

    def net_input(self, X): # calculates dot product of weighted lengths times actual and adds overall weight

        return np.dot(X, self.weight[1:]) + self.weight[0]

    def predict(self, X): # calculates whether the Iris is 1 or -1

        return np.where(self.net_input(X) >= 0.0, 1, -1)


'''
Below is a function that will graph out the linear difference between the two types of Iris's.
'''

def plot_decision_regions(X, y, classifier, resolution=0.02):
    

    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'light-green', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    '''

    plot the decision surface

    '''

    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    '''

    plot class samples

    '''

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1], alpha=.8, c=cmap(idx), marker=markers[idx], label=cl)


pl = Perceptron(eta=.01, n_iter=10)
pl.fit(X, y)
plt.plot(range(1, len(pl.errorsList) + 1), pl.errorsList, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of misclassifications')
plt.show()

plot_decision_regions(X, y, classifier=pl)
plt.xlabel('petal length (cm)')
plt.ylabel('septal length (cm)')
plt.legend(loc='upper left')
plt.show()
