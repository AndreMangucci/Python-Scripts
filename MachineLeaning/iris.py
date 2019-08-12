from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np


iris = load_iris()
test_idx = [0,50,100] # there is 50 example of witch label respectively starting in the table by the indexes 0,50,100

#labelsN = iris.target_names
#featuresN = iris.feature_names

#labels = iris.target[0]
#features = iris.data[0]

#traing data - uses numpy to delete the train data 
train_target = np.delete(iris.target,test_idx) 
train_data = np.delete(iris.data,test_idx,axis=0)

# print("Train data")
# print(train_target)
# print(train_data)

#test data only gets the data that was removed from the data set
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

# print("Test data")
# print(test_target)
# print(test_data)

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

expected_answer = test_target
answer = clf.predict(test_data)
print (expected_answer)
print (answer)

#Decision tree
from sklearn.externals.six import StringIO
import pydotplus as pydot
dot_data = StringIO()
tree.export_graphviz(
    clf,
    out_file=dot_data,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
    rounded=True,
    impurity=False
)

graph = pydot.graph_from_dot_data(dot_data.getvalue())
#graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")