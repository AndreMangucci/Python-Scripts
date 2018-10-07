from sklearn import tree
features = [[125,1],[140,1],[140,0],[150,0]]
labels = [1,1,0,0]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
answer = clf.predict([[180,1]])
print(answer)