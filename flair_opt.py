# code to load xlsx data and run flair optimization

# import libraries
import os
import pandas as pd
import flair
import nltk
nltk.download('punkt')

from hyperopt import hp
from flair.embeddings import *
from flair.hyperparameter.param_selection import SearchSpace, Parameter
from sklearn.model_selection import train_test_split
from flair.hyperparameter.param_selection import TextClassifierParamSelector, OptimizationValue

from flair.data import Corpus
from flair.datasets import CSVClassificationCorpus # requires up to date version of code from github
from flair.embeddings import WordEmbeddings, FlairEmbeddings, DocumentRNNEmbeddings

# import custom code to load xlsx files
import load_data


# function required to load data and save input in correct format for flair
def prep_flair_data(file_list, file_path='data/',
                    flair_data_path='flair_data/',
                    ptest=0.25, merged=False, max_sent = 5):
    # load each data file, save in the output format for flair as sentences and exs
    print("preparing data for merged: "+str(merged)+ ", max sentences: "+str(max_sent))

    if not os.path.exists(file_path):
        print("file path given in prep_flair_data does not exist: "+str(file_path))
        print("existing paths are: "+str(os.listdir()))

    if not os.path.exists(flair_data_path):
        print("flair data path does not exist: "+str(flair_data_path)+" ... creating folder")
        os.mkdir(flair_data_path)

    if not merged:
        for file_name in file_list:
            print("loading data as excerpts")
            file_excerpts_df = load_data.load_xlsx_data([file_path + file_name],
                                                        max_sentences=max_sent, as_sentences=False)
            print("loading data as sentence")
            file_sentences_df = load_data.load_xlsx_data([file_path + file_name],
                                                         max_sentences=max_sent, as_sentences=True)

            # sentences: save train.csv/test.csv/dev.csv
            data_train, data_test_dev = train_test_split(file_sentences_df,
                                                         test_size=ptest, random_state=0)
            data_test, data_dev = train_test_split(data_test_dev,
                                                   test_size=0.5, random_state=1)

            event_name = file_name.split(' - ')[0]
            outdir = flair_data_path + event_name + "-sentences/"
            if not os.path.exists(outdir):
                os.mkdir(outdir)

            # save data into files in correct format for flair
            data_train.to_csv(outdir + "train.csv")
            data_test.to_csv(outdir + "test.csv")
            data_dev.to_csv(outdir + "dev.csv")

            # excerpts: save train.csv/test.csv/dev.csv
            data_train, data_test_dev = train_test_split(file_excerpts_df,
                                                         test_size=ptest, random_state=0)
            data_test, data_dev = train_test_split(data_test_dev,
                                                   test_size=0.5, random_state=1)

            event_name = file_name.split(' - ')[0]
            outdir = flair_data_path + event_name + "-excerpts/"
            if not os.path.exists(outdir):
                os.mkdir(outdir)

            # save data into files in correct format for flair
            data_train.to_csv(outdir + "train.csv")
            data_test.to_csv(outdir + "test.csv")
            data_dev.to_csv(outdir + "dev.csv")
    else:
        file_names_list = [file_path + file_name for file_name in file_list]
        print("loading data as excerpts")
        file_excerpts_df = load_data.load_xlsx_data(file_names_list,
                                                    max_sentences=max_sent,
                                                    as_sentences=False)
        print("loading data as sentences")
        file_sentences_df = load_data.load_xlsx_data(file_names_list,
                                                     max_sentences=max_sent,
                                                     as_sentences = True)

        # sentences: save train.csv/test.csv/dev.csv
        data_train, data_test_dev = train_test_split(file_sentences_df,
                                                 test_size=ptest, random_state=0)
        data_test, data_dev = train_test_split(data_test_dev,
                                               test_size=0.5, random_state=1)

        event_name = 'merged'
        outdir = flair_data_path+event_name+"-sentences/"
        if not os.path.exists(outdir):
            os.mkdir(outdir)

        data_train.to_csv(outdir+"train.csv")
        data_test.to_csv(outdir+"test.csv")
        data_dev.to_csv(outdir+"dev.csv")

        # excerpts: save train.csv/test.csv/dev.csv
        data_train, data_test_dev = train_test_split(file_excerpts_df,
                                                 test_size=ptest, random_state=0)
        data_test, data_dev = train_test_split(data_test_dev,
                                               test_size=0.5, random_state=1)

        outdir = flair_data_path+event_name+"-excerpts/"
        if not os.path.exists(outdir):
            os.mkdir(outdir)

        data_train.to_csv(outdir+"train.csv")
        data_test.to_csv(outdir+"test.csv")
        data_dev.to_csv(outdir+"dev.csv")

if __name__ == '__main__':
    # create flair corpus
    data_path = 'data/'
    flair_data_path = 'flair_data/'
    flair_results_path = 'flair_results/'

    if not os.path.exists(data_path):
        print("data path does not exist: "+data_path)
        print("existing files are: "+str(os.listdir()))
    file_names = os.listdir(data_path)
    xlsx_files = [file_name for file_name in file_names if 'xlsx' in file_name]
    print("detected xlsx files: "+str(xlsx_files))

    if len(xlsx_files) == 0:
        print("no xlsx files in data folder: "+str(os.listdir(data_path)))

    # print("print saving prepped data for flair for individual datasets:")
    # prep_flair_data(xlsx_files,
    #                 file_path =data_path,
    #                 flair_data_path = flair_data_path,
    #                 ptest=0.25, merged = False)

    print("print saving prepped data for flair for merged datasets:")
    prep_flair_data(xlsx_files,
                    file_path = data_path,
                    flair_data_path = flair_data_path,
                    ptest=0.25, merged = True)


    flair_files = os.listdir(flair_data_path)
    print("flair data folders: "+str(os.listdir(flair_data_path)))
    flair_file = flair_files[0]

    # for first file in flair data files

    wdir = flair_results_path+flair_file+"-opt"
    print('create results folder for flair file: '+str(wdir))
    if not os.path.exists(flair_results_path):
        os.mkdir(flair_results_path)
    if not os.path.exists(wdir):
        os.mkdir(wdir)

    # create corpus:
    # column format indicating which columns hold the text and label(s)
    column_name_map = {3: "text", 4: "label_topic"}

    print('creating corpus for flair data: '+str(flair_data_path+flair_file))
    # 1. load corpus containing training, test and dev data and if CSV has a header, you can skip it
    corpus: Corpus = CSVClassificationCorpus(flair_data_path+flair_file, column_name_map,
                                             test_file='test.csv',
                                             dev_file='dev.csv',
                                             train_file='train.csv',
                                             skip_header=True)

    # 2. create the label dictionary
    print("create label dict")
    label_dict = corpus.make_label_dictionary()


    # define search space
    print("define search space")
    search_space = SearchSpace()

    # list of embeddings to try
    opt_embeddings = [[WordEmbeddings('glove')],
                      [WordEmbeddings('en-news')],
                      [BytePairEmbeddings('en')],
                      [OneHotEmbeddings(corpus)],
                      [StackedEmbeddings([WordEmbeddings('glove'),
                                          FlairEmbeddings('news-forward'),
                                          FlairEmbeddings('news-backward'),
                                          ])]#,
                      #[ELMoEmbeddings()]
                      ]
    search_space.add(Parameter.EMBEDDINGS, hp.choice, options=opt_embeddings)
    search_space.add(Parameter.HIDDEN_SIZE, hp.choice, options=[32, 64, 128])
    search_space.add(Parameter.RNN_LAYERS, hp.choice, options=[1, 2])
    search_space.add(Parameter.DROPOUT, hp.uniform, low=0.0, high=0.5)
    search_space.add(Parameter.LEARNING_RATE, hp.choice, options=[0.05, 0.1, 0.15, 0.2])
    search_space.add(Parameter.MINI_BATCH_SIZE, hp.choice, options=[8, 16, 32])

    # run optimization
    # create the parameter selector
    print("run optimaization on search space")
    param_selector = TextClassifierParamSelector(
        corpus = corpus,
        multi_label = False,
        base_path = wdir,
        document_embedding_type ='lstm',
        max_epochs=100,
        training_runs=3,
        optimization_value=OptimizationValue.DEV_SCORE
    )

    # start the optimization
    param_selector.optimize(search_space, max_evals=100)