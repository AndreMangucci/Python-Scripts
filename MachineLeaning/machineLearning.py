from sklearn import tree
features = [[125,1],[140,1],[140,0],[150,0]] #characteristics, in this case fruit weight followed by texture, 1 for smooth and 0 for bumpy
labels = [1,1,0,0] #data label 1 for apple and 0 for orange 
clf = tree.DecisionTreeClassifier() #it create a empty decision tree
clf = clf.fit(features,labels) #find patterns in the provided features to create rules for the decision tree
answer = clf.predict([[180,1]])
print(answer)