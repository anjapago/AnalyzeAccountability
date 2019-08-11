import pyLDAvis
import json
import nltk
import numpy as np
import pandas as pd

from nltk.stem import snowball
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist
from itertools import compress
import load_data

nltk.download('punkt')
nltk.download('stopwords')

def stem_tokenizer(doc):
    tokens = word_tokenize(doc)
    stemmer = snowball.SnowballStemmer("english", ignore_stopwords=True)
    stemmed_tokens = [stemmer.stem(word) for word in tokens]
    return([tok.lower() for tok in stemmed_tokens if tok.isalpha()])



def produce_visualization(file_names = ["Isla Vista - All Excerpts - 1_2_2019.xlsx"],
                            tokenizer = stem_tokenizer, labels = ['ACCOUNT', 'HERO'],
                            display = True):
    data = load_data.load_xlsx_data(file_names,
                                    max_sentences = None,
                                    as_sentences = False,
                                    labels=labels)

    excerpts = list(data['Excerpts'])

    # create a subset of the data frame that is the account label types
    main_types_df = data[labels]

    main_types_df.index = range(1, main_types_df.shape[0]+1)

    # drop rows and excerpts with no label
    # build vocab and doc_lengths
    all_words = []
    doc_lengths = []
    main_types_excerpts = []
    for idx, doc in enumerate(excerpts):
        if sum(main_types_df.loc[idx+1]) < 1:
            # if this document had no main type label
            main_types_df = main_types_df.drop([idx+1], axis = 0)
        else:
            main_types_excerpts.append(doc)
            doc_toks = stem_tokenizer(doc)
            all_words.extend(doc_toks)
            doc_lengths.append(len(doc_toks))
    fdist = FreqDist(all_words)
    fdistmc = fdist.most_common()
    vocab = [word for word, count in fdistmc]
    term_frequency = [count for word, count in fdistmc]
    print("number of documents: "+str(len(doc_lengths)))

    # build topic-term distribution
    stop_words = set(stopwords.words('english'))
    freq_dist_dict = {}
    topic_size = []
    topic_num_words = []
    i=0
    for coln in main_types_df.columns:
        categ_excerpts = list(compress(main_types_excerpts, main_types_df[coln].values))
        exq = [stem_tokenizer(doc) for doc in categ_excerpts]
        excerpt_words = [tok for tok_list in exq for tok in tok_list]
        i=i+1
        topic_size.append(len(exq))
        topic_num_words.append(len(excerpt_words))
        print("Topic "+str(i)+": "+coln+" number of excerpts: "+str(len(exq)))
        words = [word for word in excerpt_words if word.lower() not in stop_words and word.isalpha()]
        freq_dist_dict[coln] = FreqDist(words)

    topic_term_dists = []

    for coln in main_types_df.columns:
        ffdist = freq_dist_dict[coln]
        fdist = [ffdist.freq(word) if word in ffdist.keys()
         else np.nextafter(float(0), (1)) for word in vocab]
        #print("categ: "+str(coln)+" len of freq dist "+str(len(fdist))+" sum of vetor: "+str(sum(fdist)))
        topic_term_dists.append([float(i) for i in fdist])

    # Document-topic distribution
    doc_topic_dists = []
    for index, rowi in main_types_df.iterrows():
        row = list(rowi)
        if(sum(row)>1.01 or sum(row)<0.99):
            #print(str(index)+" row: "+str(row))
            # normalize row
            row = [r/sum(row) for r in row]
        if(sum(row)==0):
            print(row)
        doc_topic_dists.append([float(i) for i in row])

    # format for pyLDAvis
    data_dict = {'topic_term_dists': topic_term_dists,
                'doc_topic_dists': doc_topic_dists,
                'doc_lengths': doc_lengths,
                'vocab': vocab,
                'term_frequency': term_frequency}
    #print('Topic-Term shape: %s' % str(np.array(data_dict['topic_term_dists']).shape))
    #print('Doc-Topic shape: %s' % str(np.array(data_dict['doc_topic_dists']).shape))

    # save data as json
    with open('viz.json', 'w') as json_file:
        json.dump(data_dict, json_file)

    vis_data = pyLDAvis.prepare(**data_dict)

    # order the columns for pyldavis
    col_order = vis_data.topic_order
    categs = list(main_types_df.columns)
    string_list = [""]*len(col_order)
    for idx, i in enumerate(col_order):
        msg = "Topic "+str(idx+1)+": "+categs[i-1]+", number of words: "+str(topic_num_words[i-1])
        print(msg)
        string_list[idx] = msg

    pyLDAvis.save_html(vis_data, 'viz.html')
    if display:
        pyLDAvis.display(vis_data)
    else:
        return vis_data

if __name__ == '__main__':
    vis_data = produce_visualization(file_names = ["notebooks/data/Isla Vista - All Excerpts - 1_2_2019.xlsx"],
                                tokenizer = stem_tokenizer, labels = ['ACCOUNT', 'HERO'],
                                display = False)
