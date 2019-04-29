#!/usr/bin/python3

import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

import gensim
from sklearn.cluster import KMeans
from sklearn import cluster
from gensim.models import Word2Vec
from nltk.cluster import KMeansClusterer, euclidean_distance
from sklearn import metrics
from sklearn.metrics import silhouette_score
import warnings
warnings.filterwarnings("ignore")

df  = pd.read_csv('data_job_posts.csv', encoding="latin-1")

# Q2(B)
col_Title = df['Title']
col_Duration = df['Duration']
col_Location = df['Location']
col_JobDescription = df['JobDescription']
col_JobRequirment = df['JobRequirment']
col_RequiredQual = df['RequiredQual']
col_Salary = df['Salary']
col_Deadline = df['Deadline']
col_AboutC = df['AboutC']
print (col_Title)


# Q2(C) print the company with the highest ad
current_Year = 2015
pastTwoyears = df[df['Year'].between(current_Year-2,current_Year-1, inclusive=True)]
print (pastTwoyears.Company.value_counts().nlargest(1))


# Q2(D)
# print the month with largest job ad
print (df['Month'].value_counts().nlargest(1))


# Q2(E)
stop_words = set(stopwords.words('english'))
porter_stemmer = PorterStemmer()

df['JobRequirment'] = df.JobRequirment.str.replace("[^\w\s]", "").str.lower()
df['JobRequirment'] = df['JobRequirment'].dropna().apply(lambda x: [item for item in x.split() if item not in stop_words])
df['JobRequirment']=df['JobRequirment'].dropna().apply(lambda x : [porter_stemmer.stem(y) for y in x])

# Q2(F)
def replace_custom():
	CUSTOM = "Hello"
	df['JobRequirment'] = df['JobRequirment'].fillna(CUSTOM)
	df['JobDescription'] = df['JobDescription'].fillna(CUSTOM)
	df['Title'] = df['Title'].fillna(CUSTOM)
replace_custom()

# Q2(G) Output the output from q2 as dataFrame
Data_V2 = pd.DataFrame(df, columns = ['JobRequirment', 'JobDescription','Title'])

# Output as CSV
Data_V2.to_csv('Output_Q2PuncStopStem.csv') 



# Q3(A)
NUM_CLUSTERS=15

all_words=[]

for i, row in Data_V2.iterrows():
    comment = row['JobRequirment']
    #comment_all_words = nltk.tokenize.regexp_tokenize(comment, r'\w+')
    all_words.append(comment)

model_2 = Word2Vec(all_words, min_count=1)
X = model_2[model_2.wv.vocab]

#clustering with random seeds
kclusterer = KMeansClusterer(NUM_CLUSTERS, euclidean_distance, repeats=25, avoid_empty_clusters=True)
assigned_clusters = kclusterer.cluster(X, assign_clusters=True)


content=list()
MyEmptydf = pd.DataFrame()
df_cluster = pd.DataFrame(columns=['Terms', 'Cluster'])
words = list(model_2.wv.vocab)
for i, word in enumerate(words):
	df_cluster = df_cluster.append({'Terms': word,'Cluster': str(assigned_clusters[i])}, ignore_index=True)

print("second")
print(df_cluster.shape)
print(df_cluster.head(20))



# Q3 (B)
# sort 2nd column - ascending order
df_cluster.sort_values(by=['Cluster'], inplace=True)

df_cluster.to_csv('Output_Q3_ClusterJobDescripOR_requiremt.csv') 


