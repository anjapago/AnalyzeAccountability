import nltk
import random
import string
import time
import os
import numpy as np
import pandas as pd
from sklearn import metrics
import bert
from bert import tokenization
import tensorflow as tf
import tensorflow_hub as hub
from nltk import pos_tag, sent_tokenize
from nltk.corpus import wordnet, stopwords
from nltk.stem import snowball, WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import classification_report, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn import svm
from sklearn.pipeline import make_pipeline
import warnings
warnings.filterwarnings('ignore')


def print_report(pipe):
    y_test = data_test.ACCOUNT
    y_pred = pipe.predict(data_test.Excerpts)
    report = metrics.classification_report(y_test, y_pred)#, target_names=twenty_test.target_names)
    print(metrics.confusion_matrix(y_test, y_pred))
    print(report)
    print("accuracy: {:0.3f}".format(metrics.accuracy_score(y_test, y_pred)))

def stem_tokenizer(doc):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(doc)
    stemmer = snowball.SnowballStemmer("english", ignore_stopwords=True)
    stemmed_tokens = [stemmer.stem(word) for word in tokens]
    list_tokens = [tok.lower() for tok in stemmed_tokens if tok.isalpha()]
    return(' '.join(list_tokens))

def process_into_sentences(data_df):
    sentences = []
    account_labels = []
    original_file = []
    docid = []
    excerpt_lengths = []
    excerpt_len_sent_df = []

    for index, row in data_df.iterrows():
        excerpt = row['Excerpts']
        excerpt_sentences = sent_tokenize(excerpt)
        labels = [row['ACCOUNT']] * len(excerpt_sentences)  # add same label for each sentence
        StoryIDs = [row['StoryID']] * len(excerpt_sentences)  # add same label for each sentence
        files = [row['file']] * len(excerpt_sentences)  # add same label for each sentence
        excerpt_lengths.append(len(excerpt_sentences))
        excerpt_len_sent_df.extend([len(excerpt_sentences)] * len(excerpt_sentences))

        sentences.extend(excerpt_sentences)

        account_labels.extend(labels)
        original_file.extend(files)
        docid.extend(StoryIDs)

    sentences_dict = {'file': original_file, 'StoryID': docid,
                      'Sentences': sentences, 'ACCOUNT': account_labels,
                      'excerpt_length': excerpt_len_sent_df}

    sentences_df = pd.DataFrame(sentences_dict)
    return sentences_df

# load data from xlsx
def load_xlsx_data(file_names = ["data/Isla Vista - All Excerpts - 1_2_2019.xlsx",
                                "data/Marysville - All Excerpts - Final - 1_2_2019.xlsx",
                                "data/Newtown - All Excerpts - 1-2-2019.xlsx",
                                "data/Charleston - All Excerpts - 7_15_2019.xlsx",
                                "data/Orlando - All Excerpts - 7_15_2019.xlsx",
                                "data/San Bernardino - All Excerpts - 7_15_2019.xlsx",
                                "data/Vegas - All Excerpts - 7_15_2019.xlsx"],
                   max_sentences = None, as_sentences = False):
    excerpts = []
    account_labels = []
    original_file = []
    docid = []
    for file_name in file_names:
        if 'xlsx' in file_name:
            data = pd.read_excel(file_name, sheet_name='Dedoose Excerpts Export')
        else:
            print("wrong file type, input xlsx")
            break

        data = data.dropna(axis=0)
        ex_col = [colname if "excerpt" in colname.lower() else "" for colname in data.columns]
        ex_col = "".join(ex_col)

        excerpts.extend(list(data[ex_col]))
        labels = [1 if label =="True"  else label for label in data['ACCOUNT']]
        labels = [0 if label =="False" else label for label in labels]
        labels = [int(label) for label in labels]
        account_labels.extend(labels)
        original_file.extend([file_name]*len(data[ex_col]))
        docid.extend(list(data['StoryID']))

    short_excerpts = []
    short_account_labels = []
    short_original_file = []
    short_docid = []
    if max_sentences is not None: # filter outlong excerpts
        for idx, excerpt in enumerate(excerpts):
            excerpt_sentences = sent_tokenize(excerpt)
            if len(excerpt_sentences) < max_sentences:
                short_excerpts.append(excerpt)
                short_account_labels.append(account_labels[idx])
                short_original_file.append(original_file[idx])
                short_docid.append(docid[idx])
        account_labels = short_account_labels
        original_file = short_original_file
        docid = short_docid
        excerpts = short_excerpts

    output_data = pd.DataFrame({'file':original_file, 'StoryID': docid, 'Excerpts': excerpts, 'ACCOUNT': account_labels})
    print("num excerpts loaded: "+str(len(excerpts)))
    print(str(len(account_labels))+str(len(original_file))+str(len(docid)))

    if as_sentences:
        output_data = process_into_sentences(output_data)

    return output_data

# load processed data from csv
def load_csv_data(file_names = ["data/short_excerpts_df.csv"]):
    excerpts = []
    account_labels = []
    original_file = []
    docid = []
    for file_name in file_names:
        if 'csv' in file_name:
            data = pd.read_csv(file_name, encoding='utf-8')
        else:
            print("wrong file type, please use csv")

        ex_col = "Sentences"

        excerpts.extend(list(data[ex_col]))
        labels = [1 if label =="True"  else label for label in data['ACCOUNT']]
        labels = [0 if label =="False" else label for label in labels]
        labels = [int(label) for label in labels]
        account_labels.extend(labels)
        original_file.extend([file_name]*len(data[ex_col]))
        docid.extend(list(data['StoryID']))

    output_data = {'file':original_file, 'StoryID': docid, 'Excerpts': excerpts, 'ACCOUNT': account_labels}
    return pd.DataFrame(output_data)


def find_best_classifier(file_names):

    if 'csv' in str(file_names):
        data = load_csv_data(file_names)
    else:
        data = load_xlsx_data(file_names)
    account_labels = data['ACCOUNT']
    excerpts = data['Excerpts']

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
            try:
                f1s = f1_score(y_test,y_pred)
            except:
                return y_test, y_pred
            f1.append(f1s)
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


# This is a path to an uncased (all lowercase) version of BERT
BERT_MODEL_HUB = "https://tfhub.dev/google/bert_uncased_L-12_H-768_A-12/1"

def create_tokenizer_from_hub_module():
    """Get the vocab file and casing info from the Hub module."""
    with tf.Graph().as_default():
        bert_module = hub.Module(BERT_MODEL_HUB)
        tokenization_info = bert_module(signature="tokenization_info", as_dict=True)
        with tf.Session() as sess:
            vocab_file, do_lower_case = sess.run([tokenization_info["vocab_file"],
                                                tokenization_info["do_lower_case"]])

    return bert.tokenization.FullTokenizer(
        vocab_file=vocab_file, do_lower_case=do_lower_case)


def create_custom_tokenizer(punct = True, numbers=False):
    tokenizer = create_tokenizer_from_hub_module()
    def custom_tokenizer(text):
        tok_text = tokenizer.tokenize(text)
        if not numbers:
            tok_text = [tok for tok in tok_text if not tok.isnumeric()]
        if not punct:
            tok_text = [tok for tok in tok_text if not all(c in string.punctuation for c in tok)]
        return tok_text
    return custom_tokenizer

def gen_tfidf_vectorizers_dict():
    cust_tok_only_alpha = create_custom_tokenizer(punct=False, numbers=False)
    cust_tok_no_nums = create_custom_tokenizer(punct=True, numbers=False)
    cust_tok_all_chars = create_custom_tokenizer(punct=True, numbers=True)

    cust_tokenizers_dict = {'cust_all': cust_tok_all_chars,
                            'cust_no_nums': cust_tok_no_nums,
                            'cust_only_alpha': cust_tok_only_alpha}
    vectorizers_dict = {}

    for cust_tok_name in cust_tokenizers_dict.keys():
        cust_tokenizer = cust_tokenizers_dict[cust_tok_name]

        cust_vectorizer = TfidfVectorizer(tokenizer=cust_tokenizer,
                                          ngram_range=(1, 3), min_df=10, max_df=0.9)
        vec_name = cust_tok_name + "-3gram"
        vectorizers_dict[vec_name] = cust_vectorizer

        cust_vectorizer = TfidfVectorizer(tokenizer=cust_tokenizer,
                                          ngram_range=(1, 1), min_df=10, max_df=0.9)
        vec_name = cust_tok_name + "-1gram"
        vectorizers_dict[vec_name] = cust_vectorizer

    # add vectorizers with regular, and character based pre-processing
    vectorizers_dict['3gram'] = TfidfVectorizer(ngram_range=(1, 3), min_df=10, max_df=0.9)
    vectorizers_dict['1gram'] = TfidfVectorizer(ngram_range=(1, 1), min_df=10, max_df=0.9)
    vectorizers_dict['char'] = TfidfVectorizer(ngram_range=(3, 10), min_df=10, max_df=0.9, analyzer='char')

    return vectorizers_dict

def gen_classifiers_dict():
    logregb = LogisticRegressionCV(class_weight='balanced')
    logreg = LogisticRegressionCV()
    clf = svm.SVC(kernel='linear', class_weight = 'balanced', probability=True) # Linear Kernel
    rf = RandomForestClassifier(n_estimators=500, random_state=0, class_weight="balanced")
    abc = AdaBoostClassifier(n_estimators=50, base_estimator=clf, learning_rate=1)

    classifiers_dict = {'logregcv_balanced': logregb, 'logregcv': logreg,
                        'svm_balanced':clf, 'random_forest_balanced':rf}
                        #'adaboost_svm': abc}
    return classifiers_dict


def run_classifiers(data_train, data_test, vectorizers_dict, classifiers_dict):
    results = pd.DataFrame(columns=['classifier', 'vectorizer', 'precision', 'recall', 'fscore'])

    for classifier_name in classifiers_dict.keys():
        start_time = time.time()
        clf = classifiers_dict[classifier_name]
        for vec_name in vectorizers_dict.keys():
            # train
            vec = vectorizers_dict[vec_name]
            pipe = make_pipeline(vec, clf)
            pipe.fit(data_train.Excerpts, data_train.ACCOUNT)

            # test
            y_test = data_test.ACCOUNT
            y_pred = pipe.predict(data_test.Excerpts)
            precision, recall, fscore, support \
                = metrics.precision_recall_fscore_support(y_test, y_pred, average='binary', pos_label=1)

            # save results
            results_row = {'classifier':classifier_name, 'vectorizer':vec_name,
                           'precision': precision, 'recall': recall, 'fscore':fscore}
            print(results_row)
            results = results.append(results_row, ignore_index=True)
            end_time = time.time()
        print("Time for classifier=" + classifier_name + " : " + str(end_time - start_time))

    return results

def run_classifiers_cv(file_names, ptest=0.2, cv = 3, max_sentences = 4, as_sentences = False):
    if 'csv' in str(file_names):
        data = load_csv_data(file_names)
    else:
        data = load_xlsx_data(file_names, max_sentences=max_sentences, as_sentences=as_sentences)

    vectorizers_dict = gen_tfidf_vectorizers_dict()
    classifiers_dict = gen_classifiers_dict()

    cv_results_df = pd.DataFrame(columns = ['cv', 'classifier', 'vectorizer',
                                            'precision', 'recall', 'fscore'])

    random.seed(a=3)
    for c in range(cv):
        print("*****************START CV="+str(c)+"************************")
        start_time=time.time()
        rand_int = random.randint(0, 1000)
        data_train, data_test = train_test_split(pd.DataFrame(data),
                                                 test_size=ptest, random_state=rand_int)
        results = run_classifiers(data_train, data_test,
                                  vectorizers_dict, classifiers_dict)
        results['cv'] = pd.Series([c]*results.shape[1])
        cv_results_df = cv_results_df.append(results, ignore_index=True)
        end_time = time.time()
        print("Time for cv="+str(c)+" : "+str(end_time-start_time))

    return cv_results_df


if __name__ == '__main__':

    # for file_name in os.listdir('data/'):
    #     if 'xlsx' in str(file_name):
    #         print("==============================="+file_name+"===============================")
    #         results = run_classifiers_cv(["data/"+file_name], max_sentences=4)
    #         results.to_csv(file_name+"_excerpt_tfidf_cv_results.csv")

    for file_name in os.listdir('data/'):
        if 'xlsx' in str(file_name):
            print("==============================="+file_name+"===============================")
            results = run_classifiers_cv(["data/"+file_name], max_sentences=4, as_sentences=True)
            results.to_csv(file_name+"_sentences_tfidf_cv_results.csv")

