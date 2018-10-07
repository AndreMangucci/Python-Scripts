from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np


iris = load_iris()
test_idx = [0,50,100] # there is 50 example of witch label respectively starting in the table by the indexes 0,50,100

#labelsN = iris.target_names
#featuresN = iris.feature_names

#labels = iris.target[0]
#features = iris.data[0]

#traing data
train_target = np.delete(iris.target,test_idx) 
train_data = np.delete(iris.data,test_idx,axis=0)

#test data 
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)


expected_answer = test_target
answer = clf.predict(test_data)
print (expected_answer)
print (answer)