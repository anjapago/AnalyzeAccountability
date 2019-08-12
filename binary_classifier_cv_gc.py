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
from load_data import load_xlsx_data
import warnings
warnings.filterwarnings('ignore')


def stem_tokenizer(doc):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(doc)
    stemmer = snowball.SnowballStemmer("english", ignore_stopwords=True)
    stemmed_tokens = [stemmer.stem(word) for word in tokens]
    list_tokens = [tok.lower() for tok in stemmed_tokens if tok.isalpha()]
    return(' '.join(list_tokens))

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


def run_classifiers(data_train, data_test, vectorizers_dict, classifiers_dict, label = 'ACCOUNT'):
    results = pd.DataFrame(columns=['classifier', 'vectorizer', 'precision', 'recall', 'fscore', 'label'])

    for classifier_name in classifiers_dict.keys():
        start_time = time.time()
        clf = classifiers_dict[classifier_name]
        for vec_name in vectorizers_dict.keys():
            # train
            vec = vectorizers_dict[vec_name]
            pipe = make_pipeline(vec, clf)
            pipe.fit(data_train.Excerpts, data_train[label])

            # test
            y_test = data_test[label]
            y_pred = pipe.predict(data_test.Excerpts)
            precision, recall, fscore, support \
                = metrics.precision_recall_fscore_support(y_test, y_pred, average='binary', pos_label=1)

            # save results
            results_row = {'classifier':classifier_name, 'vectorizer':vec_name,
                           'precision': precision, 'recall': recall, 'fscore':fscore,
                           'label': label}
            print(results_row)
            results = results.append(results_row, ignore_index=True)
            end_time = time.time()
        print("Time for classifier=" + classifier_name + " : " + str(end_time - start_time))

    return results

def run_classifiers_cv(file_names, ptest=0.2, cv = 3, max_sentences = 4, as_sentences = False,
                       labels = ['ACCOUNT']):

    data = load_xlsx_data(file_names, max_sentences=max_sentences, as_sentences=as_sentences,
                          labels=labels)

    vectorizers_dict = gen_tfidf_vectorizers_dict()
    classifiers_dict = gen_classifiers_dict()

    cv_results_df = pd.DataFrame(columns = ['cv', 'classifier', 'vectorizer',
                                            'precision', 'recall', 'fscore', 'label',
                                            'num_train_exs', 'num_test_exs'])

    random.seed(a=3)
    for c in range(cv):
        print("*****************START CV="+str(c)+"************************")
        start_time=time.time()
        rand_int = random.randint(0, 1000)
        data_train, data_test = train_test_split(pd.DataFrame(data),
                                                 test_size=ptest, random_state=rand_int)
        for label in labels:
            if sum(data_train[label]) == 0 or sum(data_test[label]) ==0:
                print("0 examples of label: "+label)
            if any(data_train[label] > 1):
                print("given labels invalid: " + label)
            else:
                results = run_classifiers(data_train, data_test,
                                          vectorizers_dict, classifiers_dict,
                                          label=label)
                results['cv'] = pd.Series([c]*results.shape[1])
                results['num_train_exs'] = pd.Series([data_train[label]] * results.shape[1])
                results['num_test_exs'] = pd.Series([data_test[label]] * results.shape[1])
                cv_results_df = cv_results_df.append(results, ignore_index=True)
        end_time = time.time()
        print("Time for cv="+str(c)+" : "+str(end_time-start_time))

    return cv_results_df


if __name__ == '__main__':
    #to solve ssl error: https: // stackoverflow.com / questions / 42098126 / mac - osx - python - ssl - sslerror - ssl - certificate - verify - failed - certificate - verify

    # for file_name in os.listdir('data/'):
    #     if 'xlsx' in str(file_name):
    #         print("==============================="+file_name+"===============================")
    #         results = run_classifiers_cv(["data/"+file_name], max_sentences=4)
    #         results.to_csv(file_name+"_excerpt_tfidf_cv_results.csv")

    file_names = []
    results_path = ''
    labels = ['HERO', 'RACECULTURE', 'RESOURCES', 'SAFETY',
              'SOCIALSUPPORT', 'THREAT', 'TRAUMA', 'VICTIMS',
              'ACCOUNT', 'GRIEF',
              'EVENT', 'INVESTIGATION',
              'JOURNEY', 'LEGAL', 'MEDIA',
              'MISCELLANEOUS', 'MOURNING',
              'PERPETRATOR', 'PHOTO', 'POLICY']
    for file_name in os.listdir():
        if 'xlsx' in str(file_name):
            output_filename = file_name + "_sentences_tfidf_cv_results_labels.csv"
            file_names.append(file_name)
            print("==============================="+file_name+"===============================")
            results = run_classifiers_cv([file_name], max_sentences=4, as_sentences=False,
                                         labels = labels)
            results.to_csv(results_path+output_filename)

    # run again on all the datasets together
    results = run_classifiers_cv(file_names, max_sentences=4, as_sentences=False, labels = labels)
    results.to_csv(results_path+"fulldata_excerpts_tfidf_cv_results_labels.csv")
    results = run_classifiers_cv(file_names, max_sentences=4, as_sentences=True, labels = labels)
    results.to_csv(results_path+"fulldata_sentences_tfidf_cv_results_labels.csv")

