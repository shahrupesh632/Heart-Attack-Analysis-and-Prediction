import pandas as pd
import sklearn
from sklearn.metrics import f1_score
import pickle
import preprocess

m=['logistic','KNN','Decision_Tree','Gaussian_NB','Random_Forest','SVM']
model=m.copy()
# model=[]
model[0]=pickle.load(open('logistic.pkl','rb'))
model[1]=pickle.load(open('knn.pkl','rb'))
model[2]=pickle.load(open('decision_tree.pkl','rb'))
model[3]=pickle.load(open('gaussianNB.pkl','rb'))
model[4]=pickle.load(open('random_forest.pkl','rb'))
model[5]=pickle.load(open('svm.pkl','rb'))
# inn=minor.inn
res=[]
ff1=[]
predicted=[]
# l=list()
def predict_it(inputss,X_test,y_test):
    for i in range(0,len(model)):
        # l=[]

        y_pred=(model[i].predict(X_test))
        f1=f1_score(y_test,y_pred)

        pred=model[i].predict([inputss])
        
        # res[m[i]]=pred
        ff1.append(f1)
        predicted.append(pred)
        # res[l]=f1
        l=list()
        l.append(m[i])
        l.append(f1)
        l.append(pred)

        res.append(l)
        # l.clear
    return inputss,res





