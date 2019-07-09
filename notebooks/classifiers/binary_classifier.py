import nltk
import numpy as np
import pandas as pd
from nltk import pos_tag
from nltk.corpus import wordnet, stopwords
from nltk.stem import snowball, WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import classification_report, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn import svm

#nltk.download('stopwords')
#nltk.download('punkt')

def plot_coefficients(classifier_coefs, feature_names, top_features=20, show_neg = True):
    #coef = classifier.coef_.ravel()
    coef = classifier_coefs.ravel()
    top_positive_coefficients = np.argsort(coef)[-top_features:]
    top_negative_coefficients = np.argsort(coef)[:top_features]
    # create plot
    plt.figure(figsize=(15, 5))
    if show_neg:
        top_coefficients = np.hstack([top_negative_coefficients, top_positive_coefficients])
        colors = ['red' if c < 0 else 'blue' for c in coef[top_coefficients]]
        plt.bar(np.arange(2 * top_features), coef[top_coefficients], color=colors)
        feature_names = np.array(feature_names)
        plt.xticks(np.arange(1, 1 + 2 * top_features), feature_names[top_coefficients], rotation=60, ha='right')
    else:
        top_coefficients = top_positive_coefficients
        plt.bar(np.arange(top_features), coef[top_coefficients])
        feature_names = np.array(feature_names)
        plt.xticks(np.arange(top_features), feature_names[top_coefficients], rotation=60, ha='right')

    plt.show()

def stem_tokenizer(doc):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(doc)
    stemmer = snowball.SnowballStemmer("english", ignore_stopwords=True)
    stemmed_tokens = [stemmer.stem(word) for word in tokens]
    list_tokens = [tok.lower() for tok in stemmed_tokens if tok.isalpha()]
    return(' '.join(list_tokens))

def load_data(file_names = ["data/Isla Vista - All Excerpts - 1_2_2019.xlsx",
                                        "data/Marysville - All Excerpts - Final - 1_2_2019.xlsx",
                                        "data/Newtown - All Excerpts - 1-2-2019.xlsx"]):


    excerpts = []
    account_labels = []
    original_file = []
    docid = []
    for file_name in file_names:
        data = pd.read_excel(file_name, sheet_name='Dedoose Excerpts Export')
        data = data.dropna(axis=0)
        #ex_col = list(data.columns)[1]
        ex_col = [colname if "Excerpts" in colname else "" for colname in data.columns]
        ex_col = "".join(ex_col)
        if ex_col is "":
            ex_col = "Sentences"
        #print("Excerpt column: "+str(ex_col))
        excerpts.extend(list(data[ex_col]))
        account_labels.extend(list(data['ACCOUNT']))
        original_file.extend([file_name]*len(data[ex_col]))
        docid.extend(list(data['StoryID']))

    output_data = {'file':original_file, 'StoryID': docid, 'Excerpts': excerpts, 'ACCOUNT': account_labels}
    return pd.DataFrame(output_data)

def find_best_classifier(file_names = ["Isla Vista - All Excerpts - 1_2_2019.xlsx",
                                        "Marysville - All Excerpts - Final - 1_2_2019.xlsx",
                                        "Newtown - All Excerpts - 1-2-2019.xlsx"]):

    excerpts = []
    account_labels = []
    for file_name in file_names:
        if 'xlsx' in file_name:
            data = pd.read_excel(file_name, sheet_name='Dedoose Excerpts Export')
        else:
            data = pd.read_csv(file_name, encoding = 'utf-8')

        data = data.dropna(axis=0)
        ex_col = [colname if "Excerpts" in colname else "" for colname in data.columns]
        ex_col = "".join(ex_col)
        if ex_col is "":
            ex_col = "Sentences"

        excerpts.extend(list(data[ex_col]))
        account_labels.extend(list(data['ACCOUNT']))


    # stem + count
    docs = [stem_tokenizer(doc) for doc in excerpts]
    count_vectorizer = CountVectorizer(max_features=1000, min_df=10, max_df=0.7,
                                        stop_words=stopwords.words('english'))
    stem_count_X = count_vectorizer.fit_transform(docs).toarray()

    # stem + tfidf
    docs = [stem_tokenizer(doc) for doc in excerpts]
    tfidf_vectorizer = TfidfVectorizer(max_features=1000, min_df=10, max_df=0.7,
                                        stop_words=stopwords.words('english'))
    stem_tfidf_X = tfidf_vectorizer.fit_transform(docs).toarray()

    doc_vectors = {'vectorizers':[count_vectorizer, tfidf_vectorizer],
                    'vectors':[stem_count_X, stem_tfidf_X],
                    'type':["count vector", "tfidf vector"]}

    #Create a svm Classifier
    clf = svm.SVC(kernel='linear', class_weight = 'balanced') # Linear Kernel
    logreg = LogisticRegression(solver='lbfgs', max_iter=1000, class_weight='balanced')
    rf = RandomForestClassifier(n_estimators=500, random_state=0, class_weight="balanced")

    classifiers = [clf, logreg, rf]
    classifier_f1s = []
    classifier_best_vecs = []
    classifier_best_vectorizer = []

    for classi in classifiers:
        f1 = []
        y_preds = []
        print("Processing classifier: "+str(type(classi).__name__))
        for doc_vector in doc_vectors['vectors']:
            docs_train, docs_test, y_train, y_test \
            = train_test_split(pd.DataFrame(doc_vector), account_labels,
                                test_size=0.25, random_state=50)

            classi.fit(docs_train, y_train)
            y_pred = classi.predict(docs_test)
            f1.append(f1_score(y_test,y_pred))
            y_preds.append(y_pred)

        print("Classifier: "+str(type(classi).__name__)+" f1: "+str(f1))

        best_vec = np.argmax(f1)
        print(doc_vectors['type'][best_vec]+" "+str(type(classi).__name__)+" results:")
        print(confusion_matrix(y_test,y_preds[best_vec]))
        print(classification_report(y_test,y_preds[best_vec]))
        classifier_f1s.append(max(f1))
        classifier_best_vecs.append(doc_vectors['vectors'][best_vec])
        classifier_best_vectorizer.append(doc_vectors['vectorizers'][best_vec])

    best_classi_id = np.argmax(classifier_f1s)
    best_classi = classifiers[best_classi_id]
    best_vecs = classifier_best_vecs[best_classi_id]
    best_vectorizer = classifier_best_vectorizer[best_classi_id]

    docs_train, docs_test, y_train, y_test \
    = train_test_split(pd.DataFrame(best_vecs), account_labels,
                        test_size=0.2, random_state=0)

    best_classi.fit(docs_train, y_train)
    y_pred = best_classi.predict(docs_test)
    results = {"predicted":y_pred, "actual":y_test,
                "test_vectors":docs_test,
                'test_excerpts': [excerpts[idx] for idx in list(docs_test.index)],
                "classifier":best_classi,
                "vectorizer": best_vectorizer, "vectors":best_vecs}
    return results

if __name__ == '__main__':
    results = find_best_classifier()
