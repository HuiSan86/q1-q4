import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
from gensim.models import Word2Vec
import nltk
import gensim


# Q3 (A)
file = gensim.models.word2vec.Text8Corpus('./text8')
model = gensim.models.Word2Vec(file, size=100)
model.save('./text-8_gensim')

df = pd.read_csv('./Output_Q2.csv', encoding="latin-1")
original_df = pd.DataFrame(df)


#prepare the data in correct format for clustering: Column used: JobDescription
final_data = []
print(type(df))
for i, row in df.iterrows():
    comment_vectorized = []
    comment = row['JobDescription']
    comment_all_words = nltk.tokenize.regexp_tokenize(comment, r'\w+')

    for comment_w in comment_all_words:
        try:
            comment_vectorized.append(list(model[comment_w]))
        except Exception as e:
            pass
    try:
        comment_vectorized = np.asarray(comment_vectorized)
        comment_vectorized_mean = list(np.mean(comment_vectorized, axis=0))
    except Exception as e:
        comment_vectorized_mean = list(np.zeros(100))
        pass
    try:
        len(comment_vectorized_mean)
    except:
        comment_vectorized_mean = list(np.zeros(100))
    temp_row = np.asarray(comment_vectorized_mean)
    final_data.append(temp_row)
X = np.asarray(final_data)
print('Conversion to array complete') 
print('Clustering Comments')
#perform clustering
clf = KMeans(n_clusters=4, n_jobs=-1, max_iter=50000, random_state=1)
clf.fit(X)
print('Clustering complete')


# Add the cluster label in original dataframe under new CLASS column and save the csv file
comment_label = clf.labels_
comment_cluster_df = pd.DataFrame(original_df)
comment_cluster_df['CLASS'] = np.nan
comment_cluster_df['CLASS'] = comment_label
print('Saving to csv')

# Q3 (B) Output top group
comment_cluster_df.to_csv('./Clustering_q3.csv', index=False)
