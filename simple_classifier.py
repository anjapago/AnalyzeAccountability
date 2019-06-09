import nltk
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

nltk.download('stopwords')
nltk.download('punkt')

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


# stem + tfidf
docs = [stem_tokenizer(doc) for doc in excerpts]
vectorizer = TfidfVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
stem_tfidf_X = vectorizer.fit_transform(docs).toarray()

docs_train, docs_test, y_train, y_test = train_test_split(stem_count_X, list(data['ACCOUNT']),
                                                          test_size=0.2, random_state=0)
#Create a svm Classifier
clf = svm.SVC(kernel='linear') # Linear Kernel
#Train the model using the training sets
clf.fit(docs_train, y_train)

y_pred = clf.predict(docs_test)
print("count vector SVM results")
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))

docs_train, docs_test, y_train, y_test = train_test_split(stem_tfidf_X, list(data['ACCOUNT']),
                                                          test_size=0.2, random_state=0)
#Create a svm Classifier
clf = svm.SVC(kernel='linear') # Linear Kernel
#Train the model using the training sets
clf.fit(docs_train, y_train)

y_pred = clf.predict(docs_test)
print("tfidf vector SVM results")
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))

docs_train, docs_test, y_train, y_test = train_test_split(stem_count_X, list(data['ACCOUNT']),
                                                          test_size=0.2, random_state=0)

logreg = LogisticRegression(solver='lbfgs', max_iter=1000)
logreg.fit(docs_train, y_train)

y_pred = logreg.predict(docs_test)
print("count vector logistic regression results")
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))


docs_train, docs_test, y_train, y_test = train_test_split(stem_count_X, list(data['ACCOUNT']), #test_size=0.2,
                                                         random_state=0)
classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
classifier.fit(docs_train, y_train)


y_pred = classifier.predict(docs_test)
print("count vector random forest results")
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))

print(len(classifier.feature_importances_) == len(vectorizer.get_feature_names()))
top_feats = np.argsort(classifier.feature_importances_)[-10:]
feat_names = [vectorizer.get_feature_names()[feat] for feat in top_feats]
print(feat_names)

test_doc = np.zeros(len(docs_test[1]))
test_doc[top_feats[6]] = 1
print("class: "+str(classifier.predict([test_doc])))
