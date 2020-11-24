###Reading in data and getting a visualization
import pandas as pd 
import matplotlib as plt

#read in data
data_path = './../../riid-test-answer-prediction/'
''' Possibble Data files:
	train.csv
	questions.csv
	lectures.csv
	example_test.csv
	example_sample_submission.csv '''
df = pd.read_csv(data_path + 'train.csv')

print(df.head(10))

#visualize the data