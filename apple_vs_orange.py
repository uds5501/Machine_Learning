from sklearn import tree

#We are coding the textures as following:
#1=smooth
#0=bumpy
#features=[x,y] where x: weight in gram and y represents textures

features=[[140,1],[130,1],[150,0],[170,0]]

 # Coding the labels as 0=apple,1=orange
 
labels=[0,0,1,1]

#Creating a classifier using simple tree classification

clf=tree.DecisionTreeClassifier()

clf=clf.fit(features,labels) #fitting training data in the classifier

print clf.predict([[150,0]]) #fruit is 150g and bumpy in texture
