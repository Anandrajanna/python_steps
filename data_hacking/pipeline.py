from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5)

# Decision tree
from sklearn import tree
my_classifier = tree.DecisionTreeClassifier()

my_classifier.fit(X_train, y_train)
predictions = my_classifier.predict(X_test)
print predictions

from sklearn.metrics import accuracy_score
print "Decision tree: ", accuracy_score(y_test, predictions)

# K Nearest Neighbor
from sklearn.neighbors import KNeighborsClassifier
my_classifier = KNeighborsClassifier()

my_classifier.fit(X_train, y_train)
predictions = my_classifier.predict(X_test)
print predictions

from sklearn.metrics import accuracy_score
print "K nearest neigghbor: ", accuracy_score(y_test, predictions)
