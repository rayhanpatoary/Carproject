import pandas as pd
import numpy as np
from sklearn import pipeline,preprocessing,metrics,model_selection,ensemble
from sklearn_pandas import DataFrameMapper
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
import joblib 

# This function is called from Views.py to get the prediction based on 6 parameters
def prediction_function( cylender, displacement , horsepower , weight , acceleration , modelyear , origin ):
      carMPGmodel=joblib.load('CarMPG/MLModelforMPG.pkl') #Load our Machine Learning model 
      temp={} # creare a temporary Variable
      #assign values:
      temp['cylinders']=cylender
      temp['displacement']=displacement
      temp['horsepower']=horsepower
      temp['weight']=weight
      temp['acceleration']=acceleration
      temp['model year']=modelyear
      temp['origin']=origin
      testDtaa=pd.DataFrame({'x':temp}).transpose() # convert temporary variable to a Dataframe
      result = carMPGmodel.predict(testDtaa)[0] # Doing the prediction
      return result; # return result

print(prediction_function( 1, 2 , 3 , 4 , 5 , 6 , 7 ))






          



