import pandas as pd
import numpy as nm
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split

# Reading a file
# df =pd.read_csv('heart.csv')
def spliting(df):
    X = df.drop(['output'],axis=1)
    y = df[['output']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    return X_test,y_test

def rename_columns(df):
    return df.rename(columns={
        'age':'Age',
        'sex':'Sex',
        'exng':'Exercise Induced Angina',
        'caa':'Number of Major Vessels',
        'cp':'Chest Pain Type',
        'trtbps':'Resting Blood Pressure (mm Hg)',
        'chol' : 'Cholestoral (mg/dl)',
        'fbs':'Fasting Blood Pressure (>120 mg/dl)',
        'restecg' : 'Resting Electrocardiographic Results',
        'thalachh': 'Maximum Heart Rate Achieved',
        'oldpeak':'Previous Peak',
        'slp':'Slope',
        'thall':'Thal Rate'
    })

def category_mapping(df):
    # For Sex
    df['sex'].map({0:'Female',1:'Male'})

    # Chest pain Type
    df['cp'].map({0:'Typical Angina',1:'Atypical Angina',2:'Non-anginal Pain',3:'Asymptomatic'})
    df['cp'].map({1:'Typical Angina',2:'Atypical Angina',3:'Non-anginal Pain',4:'Asymptomatic'})

    # 'fbs'
    df['fbs'].map({0:'False',1:'True'})

    #'restecg'
    df['restecg'].map({0:'Normal',1:'ST-T wave abnormality',2:'Probable or Definite left ventricular hypertrophy'})
    #'slp'
    df['slp'].map({1:'Upsloping',2:'Flat',3:'Downsloping'})
    # 'caa'
    df['caa'].map({0:0,1:1,2:2,3:3})
    # 'thall'
    df['thall'].map({3:'Normal',6:'Fixed Defect',7:'Reversible Defect'})

def data_type(df):
    df=df.drop(df.columns[-1],axis=1)
    unique_count=df.nunique()

    count_set={x for x in unique_count}

    count_list=list(count_set)
    count_list.sort()

    category=0
    for a in count_list:
        if a<10:
            category=a

    return unique_count[unique_count<=category].keys(),unique_count[unique_count>category].keys()


def feture_classess(col):
    coll={
    "sex":['Male','Female'],
    "cp":['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'],
    "exng":['Yes','No'],
    "fbs":['True','False'],
    "restecg":['Normal', 'ST-T wave abnormality', 'Probable or Definite left ventricular hypertrophy'],
    "slp":['Upsloping', 'Flat', 'Downsloping'],
    "caa":[0,1,2,3],
    "thall":['Normal', 'Fixed Defect', 'Reversible Defect']
    }

    return coll[col] 

def rev_map(inn):

    l0=['Female','Typical Angina','False' ,'Normal', 0,'No']
    l1=['Atypical Angina','Male', 'ST-T wave abnormality', 'Upsloping', 1,'True','Yes']
    l2=['Non-anginal Pain', 'Probable or Definite left ventricular hypertrophy', 'Flat', 2]
    l3=['Asymptomatic', 'Downsloping', 'Normal', 3]
    # l4=[]
    l6=['Fixed Defect']
    l7=["Reversible Defect"]

    ii=list()
    for i in inn:
        if i in l0:
            ii.append(0)
        elif i in l1:
            ii.append(1)
        elif i in l2:
            ii.append(2)
        elif i in l3:
            ii.append(3)
        # elif i in l4:
        #     ii.append(4)
        elif i in l6:
            ii.append(6)
        elif i in l7:
            ii.append(7)
        else:
            ii.append(i)
    
    return ii


    
