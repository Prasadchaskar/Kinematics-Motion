import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('motion.pkl', 'rb'))
class_names = ['The activity is walking','The activity is running']

def predict(df):
    df = df[['wrist', 'acceleration_x', 'acceleration_y', 'acceleration_z', 'gyro_x','gyro_y', 'gyro_z']]
    predictions = model.predict(df)
    output = [class_names[class_predicted] for class_predicted in predictions]
    return output
				
