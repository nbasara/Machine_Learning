###Reading in data and getting a visualization
import pandas as pd 
import matplotlib as plt
import time 

t0 = time.time()

pd.options.display.max_rows = 2000
#read in data
data_path = './../../riid-test-answer-prediction/'
''' Possibble Data files:
	train.csv waring reading will take 158s
	questions.csv
	lectures.csv
	example_test.csv
	example_sample_submission.csv '''
df = pd.read_csv(data_path + 'train.csv')

print(df.head(10))

t1 = time.time()

total = t1-t0
print(total)
#visualize the data