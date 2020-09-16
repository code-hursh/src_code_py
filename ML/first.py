from sklearn import tree

features = [[150,1],[170,1],[140,0],[130,0]]
labels = [1, 1, 0, 0]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels) # find patterns in data

# weight = int(input('enter weight:'))
# bumpy = int(input('bumpy or not 1/0:'))
fruit = ['apple','orange']
while True:

    weight = int(input('enter weight:'))
    bumpy = int(input('bumpy or not (1/0):'))

    print(fruit[clf.predict([[weight,bumpy]])[0]])
    if (input('would you like to continue?(y/n)') == 'y'):
        continue
    break


