import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

data = pd.read_csv('transformed_data.csv')
data = data.drop(['Name','Timestamp','Symbol','Sector','Symbol.1'],axis=1)
#print(data)

# iloc&#39;s arguments as referencing [rows, columns].
#X = data.iloc[:, :-1]
#y = data.iloc[:, -1]
x = pd.DataFrame(columns=['High','Low'])
y = pd.DataFrame(columns=['Open','Close'])
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.05, random_state=0)

# print(data)
# print(X_train)
# print()
# print(y_train)
# print()
# print(X_test)
# print()
# print(y_test)
#

#Create a svm Classifier
svm1 = SVC(kernel='linear') # Linear Kernel

#Train the model using the training sets
svm1.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = svm1.predict(X_test)
# print(y_pred)

# confusion matrix
print("\n Confusion matrix\n",confusion_matrix(y_test,y_pred))

# accuracy
print("\n accuracy\n",accuracy_score(y_test,y_pred))

# precision
print("\n Precision\n",precision_score(y_test,y_pred,average=None))

# recall
print("\n Recall\n",recall_score(y_test,y_pred,average=None))

# error rate = 1- accuracy