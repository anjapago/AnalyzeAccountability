import nltk
nltk.download('punkt')

import random
import string
import time
import os
import numpy as np
import pandas as pd
from sklearn import metrics
from nltk import pos_tag, sent_tokenize
from nltk.corpus import wordnet, stopwords
from nltk.stem import snowball, WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import classification_report, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.pipeline import make_pipeline
import warnings
warnings.filterwarnings('ignore')

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
    #excerpt_lengths = []
    excerpt_len_sent_df = []
    columns_dict={}
    for col in data_df.columns:
        columns_dict[col] = []

    for index, row in data_df.iterrows():
        excerpt = row['Excerpts']
        excerpt_sentences = sent_tokenize(excerpt)
        sentences.extend(excerpt_sentences)
        columns_dict['Excerpts'].extend(excerpt_sentences)
        #excerpt_lengths.append(len(excerpt_sentences))
        excerpt_len_sent_df.extend([len(excerpt_sentences)] * len(excerpt_sentences))
        # labels = [row['ACCOUNT']] * len(excerpt_sentences)  # add same label for each sentence
        # StoryIDs = [row['StoryID']] * len(excerpt_sentences)  # add same label for each sentence
        # files = [row['file']] * len(excerpt_sentences)  # add same label for each sentence
        # account_labels.extend(labels)
        # original_file.extend(files)
        # docid.extend(StoryIDs)
        for col in data_df.columns:
            if not col == 'Excerpts':
                columns_dict[col].extend([row[col]]*len(excerpt_sentences))

    # sentences_dict = {'file': original_file, 'StoryID': docid,
    #                   'Excerpts': sentences, 'ACCOUNT': account_labels,
    #                   'excerpt_length': excerpt_len_sent_df}
    columns_dict['excerpt_length'] = excerpt_len_sent_df

    sentences_df = pd.DataFrame(columns_dict)
    return sentences_df

# load data from xlsx
def load_xlsx_data(file_names = ["data/Isla Vista - All Excerpts - 1_2_2019.xlsx",
                                "data/Marysville - All Excerpts - Final - 1_2_2019.xlsx",
                                "data/Newtown - All Excerpts - 1-2-2019.xlsx",
                                "data/Charleston - All Excerpts - 7_15_2019.xlsx",
                                "data/Orlando - All Excerpts - 7_15_2019.xlsx",
                                "data/San Bernardino - All Excerpts - 7_15_2019.xlsx",
                                "data/Vegas - All Excerpts - 7_15_2019.xlsx"],
                   max_sentences = None, as_sentences = False, labels = ['ACCOUNT']):
    excerpts = []
    original_file = []
    docid = []
    #file_labels = []
    file_labels_dict = {}
    for label in labels:
        file_labels_dict[label] = []
    print("file names: "+str(file_names))
    data = None
    for file_name in file_names:
        if 'xlsx' in file_name:
            try:
                data = pd.read_excel(file_name, sheet_name='Dedoose Excerpts Export')
            except Exception as e:
                print("failed to load file: "+str(file_name))
                print(e)
        else:
            print("wrong file type, input xlsx")
            break

        if data is None:
            print("no xlsx files loaded")

        data = data.dropna(axis=0)
        ex_col = [colname if "excerpt" in colname.lower() else "" for colname in data.columns]
        ex_col = "".join(ex_col)

        excerpts.extend(list(data[ex_col]))

        #print(data.columns)
        for label in labels:
            data_colname = [l for l in data.columns if label.lower() in
                            "".join("".join(l.lower().split(' ')).split('/'))]
            data_colname = [l for l in data_colname if "_" not in l]
            data_colname = [l for l in data_colname if "\\" not in l]
            # if 'race' in label.lower():
            #     # adjusting for special label race/culture
            #     data_colname = [l for l in data.columns if "race" in l]
            if len(data_colname) ==0:
                print("no labels of type: "+label)
                label_list = [0 for l in range(data.shape[0])]
            else:
                data_label = data_colname[0]
                #print(data_colname)

                label_list = [1 if l =="True"  else l for l in data[data_label]]
                label_list = [0 if l =="False" else l for l in label_list]
                try:
                    label_list = [int(l) for l in label_list]
                except:
                    print(data[label])
            #file_labels.extend(label_list)
            file_labels_dict[label].extend(label_list)

        original_file.extend([file_name]*len(data[ex_col]))
        docid.extend(list(data['StoryID']))

    short_excerpts = []
    short_original_file = []
    short_docid = []
    short_file_labels_dict = {}
    for label in labels:
        short_file_labels_dict[label] = []
    if max_sentences is not None: # filter outlong excerpts
        for idx, excerpt in enumerate(excerpts):
            excerpt_sentences = sent_tokenize(excerpt)
            if len(excerpt_sentences) < max_sentences:
                short_excerpts.append(excerpt)
                short_original_file.append(original_file[idx])
                short_docid.append(docid[idx])
                for label in labels:
                    short_file_labels_dict[label].append(file_labels_dict[label][idx])
        file_labels_dict = short_file_labels_dict
        original_file = short_original_file
        docid = short_docid
        excerpts = short_excerpts

    excerpts_dict = {'file':original_file, 'StoryID': docid,'Excerpts': excerpts}
    #print(pd.DataFrame(excerpts_dict).shape)
    #print(pd.DataFrame(file_labels_dict).shape)
    output_data = pd.DataFrame({**file_labels_dict, **excerpts_dict})
    print("num excerpts loaded: "+str(len(excerpts)))
    #print(str(len(account_labels))+str(len(original_file))+str(len(docid)))

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

if __name__ == '__main__':
    labels = ['ACCOUNT', 'HERO', 'GRIEF',
               'EVENT', 'INVESTIGATION',
               'JOURNEY', 'LEGAL', 'MEDIA',
               'MISCELLANEOUS', 'MOURNING',
               'PERPETRATOR', 'PHOTO', 'POLICY',
               'RACECULTURE', 'RESOURCES', 'SAFETY',
               'SOCIALSUPPORT', 'THREAT', 'TRAUMA','VICTIMS']
    data_df = load_xlsx_data(file_names=["data/Isla Vista - All Excerpts - 1_2_2019.xlsx",
                               "data/Marysville - All Excerpts - Final - 1_2_2019.xlsx",
                               "data/Newtown - All Excerpts - 1-2-2019.xlsx",
                               "data/Charleston - All Excerpts - 7_15_2019.xlsx",
                               "data/Orlando - All Excerpts - 7_15_2019.xlsx",
                               "data/San Bernardino - All Excerpts - 7_15_2019.xlsx",
                               "data/Vegas - All Excerpts - 7_15_2019.xlsx"],
                   max_sentences=5, as_sentences=True, labels = labels)
    print(data_df)
