from flask import Flask,request
import pandas as pd
import numpy as np
import pickle

app= Flask(__name__)
pickle_in = open('log_model.pkl','rb')
model=pickle.load(pickle_in)

'''
url- http://127.0.0.1:5000/
output- Hello World
'''
@app.route('/')          #decorator
def hello_world():
    return "Hello World"

'''
url- http://127.0.0.1:5000/predict?age=34&sex=M&embark=C
request_type- GET
Num_Parameters- 3 (age, sex, embark)
output- prediction (0- not survived; 1- survived)
'''
@app.route('/predict')
def predict_survival():

    age=request.args.get('age')
    sex=request.args.get('sex')
    if sex=='M':
        sex=1
    else:
        sex=0

    embark=request.args.get('embark')
    #embarked = request.args.get('embarked')
    if embark=='C':
        third=0
        fourth=0
    if embark=='Q':
        third=1
        fourth=0
    if embark=='R':
        third=0
        fourth=1
    age=int(age)
    sex=int(sex)
    #embarked=int(embarked)
    #embark=int(embark)
    print(type(age))
    print(sex,embark)
    prediction = model.predict([[age, sex, third, fourth]])
    #prediction = model.predict([[34, 0, 0, 0]])
    #prediction=0
    prediction=prediction[0]
    return "The predicted value is "+ str(prediction)

'''
url- http://127.0.0.1:5000/predict_file
request_type- POST
Input- CSV file named book_hello.csv which gets stored in parameter named file
Num_Parameters- 4 (age, sex, embark, embarked)
File Input format-
Age - number
Sex -> 1- M; 0- F
Embark  Embarked   Interpretation
  0         0          C
  1         0          Q
  0         1          S
output- prediction (0- not survived; 1- survived)
'''

@app.route('/predict_file',methods=["POST"])
def predict_survival_file():

    df_test = pd.read_csv(request.files.get("file"))
    #print(df_test.Age[0])
    length=len(df_test)
    prediction=model.predict(df_test)
    #prediction=prediction[0]
    return "The predicted value for csv is "+ str(list(prediction))


'''
url- http://127.0.0.1:5000/predict_file_new
request_type- POST
Input- CSV file named book_changed.csv which gets stored in parameter named file_new
Why this function? - This csv file has input in user friendly format like sex as M/f; embark as S/Q/C.
Num_Parameters- 3 (age, sex, embark)
output- prediction (0- not survived; 1- survived)
'''
@app.route('/predict_file_new',methods=["POST"])
def predict_survival_file_new():

    df_test = pd.read_csv(request.files.get("file_new"))
    #print(df_test.Age[0])
    length=len(df_test)
    print(length)

    age=[]
    for x in df_test.Age:
        age.append(x)
    sex=[]
    for x in df_test.Sex:
        if x=='M':
            sex.append(1)
        else:
            sex.append(0)

    third=[]
    fourth=[]
    for x in df_test.Embark:
        if x=='C':
            third.append(0)
            fourth.append(0)
        if x=='Q':
            third.append(1)
            fourth.append(0)
        if x=='S':
            third.append(0)
            fourth.append(1)

    #print(third)
    prediction=[]
    for i in range(length):
        prediction.append(model.predict([[age[i],sex[i],third[i],fourth[i]]]))

    final=[]
    for i in range(length):
        final.append(prediction[i][0])

    #print(final)
    #return "Hello PD"
    return "The predicted value for csv is "+ str(list(final))

if __name__=='__main__':
    app.run(debug=True)