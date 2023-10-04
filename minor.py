import streamlit as st
import pandas as pd
import sklearn
from sklearn.metrics import f1_score
import pickle, operator
import preprocess
import models

df=pd.read_csv("heart.csv")


col1,col2,col3=st.columns([3,6,2])
with col2:
    st.header("Heart Attack Prediction")



# st.dataframe(df)

dff=preprocess.rename_columns(df)
features_dff=dff.columns
column=df.columns
features=column[:-1]

categorical_data,continuous_data=preprocess.data_type(df)

X_test,y_test=preprocess.spliting(df)

col=list()

col=st.columns(len(column)-1)
inputss={}
for i in range(0,len(column)-1):
    with st.container():
        # st.header(column[i])
        if column[i] in continuous_data:
            a=st.number_input(features_dff[i])
        elif column[i] in categorical_data:
            dat=preprocess.feture_classess(column[i])
            a=st.selectbox(features_dff[i],dat)
        inputss[column[i]]=a

col1,col2,col3=st.columns([4,3,2])
with col2:
    but=st.button("Predict")


innp=[]

for col in features:
    innp.append(inputss[col])

inn=preprocess.rev_map(innp)

# st.title("Our input is: ")
# st.markdown(inn)

if but:
    inpp,ress=models.predict_it(inn,X_test,y_test)

    a=pd.DataFrame(ress,columns=['Name','F1_Score','Predicted'])
    a=a.sort_values(by=['F1_Score'],ascending=False)
    a=pd.DataFrame(a[:-1])

    b=a.Predicted.value_counts()

    if(b.size==1):
        if b.index[0]:
            st.title("There is chance of Heart Attact")
        else:
            st.title("There isn't chance of Heart Attack")
    else:
        if b.index[0]:
            st.title("There is chance of Heart Attact")
        else:
            st.title("There isn't chance of Heart Attack")
    
    ress.clear()
