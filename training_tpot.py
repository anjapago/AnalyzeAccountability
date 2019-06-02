import numpy as np
import pandas as pd
from nltk import pos_tag
from nltk.corpus import wordnet, stopwords
from nltk.stem import snowball, WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer 
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import svm

from tpot import TPOTClassifier
from sklearn.externals.joblib import Memory

file_name = "Isla Vista - All Excerpts - 1_2_2019.xlsx"
data = pd.read_excel(file_name, sheet_name='Dedoose Excerpts Export')
print(data.shape)
data = data.dropna(axis=0)
print(data.shape)
print(data.columns)

excerpts = list(data['Excerpt'])
def stem_tokenizer(doc):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(doc) 
    stemmer = snowball.SnowballStemmer("english", ignore_stopwords=True)
    stemmed_tokens = [stemmer.stem(word) for word in tokens]
    list_tokens = [tok.lower() for tok in stemmed_tokens if tok.isalpha()]
    return(' '.join(list_tokens))
print("original: "+str(excerpts[3]))
print(stem_tokenizer(excerpts[3]))

# stem + count
docs = [stem_tokenizer(doc) for doc in excerpts]
vectorizer = CountVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))  
stem_count_X = vectorizer.fit_transform(docs).toarray() 

docs_train, docs_test, y_train, y_test = train_test_split(stem_count_X, list(data['ACCOUNT']),
                                                          test_size=0.2, random_state=0) 

tpot = TPOTClassifier(generations=100, population_size=100, verbosity=2, config_dict='TPOT sparse',
					 max_time_mins=3000, max_eval_time_mins=5, scoring = 'f1_macro', warm_start = True,
                     n_jobs = 1, periodic_checkpoint_folder='tpot_checkpoints', cv = 5, memory = 'auto')
tpot.fit(docs_train, y_train)

tpot.export('tpot_pipeline.py')

print(tpot.score(docs_test, np.array(y_test)))


