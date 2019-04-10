#!/usr/bin/python3

import re
import pandas as pd
import numpy as np

data  = pd.read_csv('data_job_posts.csv')


# Q2(B)
selec_col = pd.DataFrame(data, columns=["Title","Duration", "Location", "JobDescription", "JobRequirment", "RequiredQual", "Salary", "Deadline", "AboutC"])
print (selec_col)


# Q2(C) print the company with the highest ad
current_Year = 2015
df = pd.DataFrame(data)
pastTwoyears = df[df['Year'].between(current_Year-2,current_Year-1, inclusive=True)]
print (pastTwoyears.Company.value_counts().nlargest(1))



# Q2(D)
# print the month with largest job ad
print (data.Month.value_counts().nlargest(1))



# Q2(E)
# # Convert plural to singular and remove stop words
from sklearn.feature_extraction import text
import inflection as inf

stop_words = text.ENGLISH_STOP_WORDS
data['JobRequirment'] = data['JobRequirment'].dropna().apply(lambda x: ' '.join([inf.singularize(item) for item in x.split()]))
a = data['JobRequirment'].astype(str)

data['JobRequirment'] = a.dropna().apply(lambda x: [item for item in x.split() if item not in stop_words])
data['Job_Requirement'] = data['JobRequirment']


# Q2(F)
def replace_custom():
	CUSTOM = "Hello"
	data['Duration'] = data['Duration'].fillna(CUSTOM)
	
replace_custom()


# Also replaced NA in the remaining columns with "Hello"
def replace_emptyFill_title_loc_desc_req_quali_sal_deadl_C():
	CUSTOM = "Hello"
	data['Title'] = data['Title'].fillna(CUSTOM)
	data['Location'] = data['Location'].fillna(CUSTOM)
	data['JobDescription'] = data['JobDescription'].fillna(CUSTOM)
	data['Job_Requirement'] = data['Job_Requirement'].fillna(CUSTOM)
	data['RequiredQual'] = data['RequiredQual'].fillna(CUSTOM)
	data['Salary'] = data['Salary'].fillna(CUSTOM)
	data['Deadline'] = data['Deadline'].fillna(CUSTOM)
	data['AboutC'] = data['AboutC'].fillna(CUSTOM)

replace_emptyFill_title_loc_desc_req_quali_sal_deadl_C()


# Q2(G) Output the information as dataFrame
Data_V2 = pd.DataFrame(data, columns = ['Title','Duration', 'Location', 'JobDescription', 'Job_Requirement', 'RequiredQual', 'Salary', 'Deadline', 'AboutC'])

# Output as CSV
Data_V2.to_csv('Output_Q2.csv') 




# Q2(H)
'''
import boto3
from botocore.client import Config

ACCESS_KEY_ID = ''
ACCESS_SECRET_KEY = ''
BUCKET_NAME = 'Q2_S3'

data = open('Output_Q2.csv', 'rb')

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
s3.Bucket(BUCKET_NAME).put_object(Key='Output_Q2.csv', Body=data)
print ("Done")
'''



