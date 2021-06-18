# EDA-on-Titanic-Dataset
**Titanic.ipynb** - In this file Exploratory Data Analysis on Titanic Dataset (which is stored in train.csv) is done. Various plots amongst different columns of the dataset are made to get more understanding of the dataset. 
A logistic regression model was prepared on train.csv file data but keeping input parameters as ['Age','Sex','Embarked'] and output parameter as 'Survived'
A random forest classifier is also created but that classifier model is made just for comparison purpose with Logistic Regression model



**basic.py** - In this file a Flask API was created which can handle both GET and POST request to return the prediction done by the model named 'log_model.pkl'.
Functions -

hello_world - Just default function which execute when on running 'basic.py' file we hit the default url that is 'http://127.0.0.1:5000/'

predict_survival - This function is for handling GET request where you hit url like 'http://127.0.0.1:5000/predict?age=34&sex=M&embark=C' that is entering three paramters in url in this specified format it is going to return the prediction.

predict_survival_file - This function is for handling POST request. One can input the data in book_hello.csv file 
                        
File Input format-
Age - number
Sex -> 1- M; 0- F ||  
Embark=0; Embarked=0; Interpretation-C
Embark=1; Embarked=0; Interpretation-Q
Embark=0; Embarked=1; Interpretation-S  ||  
Output- Prediction of person will survive or not
 
predict_survival_file_new - This function is for handling POST request. One can input the data in book_changed.csv file. File input format is quite understandable in this file it                             matches with the original dataset format. Output- Prediction of person will survive or not
