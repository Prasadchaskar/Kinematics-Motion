import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('/content/sample_data/motion.pkl', 'rb'))
class_names = ['The activity is walking','The activity is running']

def predict(df):
    df = df[['wrist', 'acceleration_x', 'acceleration_y', 'acceleration_z', 'gyro_x','gyro_y', 'gyro_z']]
    predictions = model.predict(df)
    output = [class_names[class_predicted] for class_predicted in predictions]
    return output
				
wrist = 0	
acceleration_x =0.2650 	
acceleration_y = -0.7814
acceleration_z=-0.0076
gyro_x=	-0.0590	
gyro_y=0.0325
gyro_z=-2.9296

df = pd.DataFrame({ 
    'wrist':[wrist],
    'acceleration_x':[acceleration_x], 
    'acceleration_y':[acceleration_y], 
    'acceleration_z':[acceleration_z], 
    'gyro_x':[gyro_x],
    'gyro_y':[gyro_y],
    'gyro_z':[gyro_z]
})
print(predict(df))