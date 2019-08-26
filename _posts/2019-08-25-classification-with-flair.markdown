---
layout: post
title:  "Classification with Flair"
date:   2019-08-25 00:00:30 -0400
categories: update
permalink: /:categories/:year/:month/:day/:title.html
---

This post will describe the flair library and the approaches used. The classification task focussed on in these experiments is the original task of binary classification of accountability. Also, it will be applied on the sentence level (instead of the excerpt level). See previous posts for explanation of this dataset and task.

## Flair Library
[Flair](https://github.com/zalandoresearch/flair) is an open source library for natural language processing created by Zalando research. Flair is *"a very simple framework for state-of-the-art natural language processing (NLP)"*. The main benefit of this library is that it makes it easy to implement and experiment with many state of the art methods within the same framework, in particular experiments with different text representations (embeddings).  

For additional resources explaining flair, please view:
- [overview](https://www.analyticsvidhya.com/blog/2019/02/flair-nlp-library-python/)
- [text classification](https://towardsdatascience.com/text-classification-with-state-of-the-art-nlp-library-flair-b541d7add21f)
- [tutorials](https://github.com/zalandoresearch/flair/blob/master/resources/docs/TUTORIAL_7_TRAINING_A_MODEL.md)
- [presentation by zalando](http://alanakbik.github.io/talks/ML_Meetup_2018.pdf)

## Testing Flair Word Embeddings and Document Embeddings

Simple experiments were implemented in the [notebook in github]
(https://github.com/anjapago/AnalyzeAccountability/blob/master/flair_analysis.ipynb).

The first simple approach tested was document pooling and standard glove embeddings. I also tested the recommended settings of glove embeddings stacked with the flair forward and backward embeddings, and I also experimented with the document RNN and LSTM. None of the results showed a noticeable improvement in fscore. 

## Optimization Experiment

Hyperopt is used to optimize various parameters of the flair classifiers, including the choice of word-embeddings. The search space of parameters used is:

```python
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
```

The full code can be found in the [github repository](https://github.com/anjapago/AnalyzeAccountability/blob/master/flair_opt.py).

The following show the results from each evaluation run. Each evaluation run would run for 100 epochs and take around 12 hours to complete. There are 7 runs, so the code took around 3 days to produce these results, running with 16-cores. The results show the settings of each parameter, and the performance on the test set ("test_score"). The test score shown is the f score for the accountability label. The results are similar to what have seen from previous methods, including the simple sklearn vectorizers and classifiers, and with Bert, which have all acheived results in the same ball park around fscore = 0.6 for sentence based classification on accountability label.

    evaluation run 1
    	dropout: 0.005710496817261157
    	embeddings: en-fasttext-news-300d-1M
    	hidden_size: 64
    	learning_rate: 0.2
    	mini_batch_size: 32
    	rnn_layers: 2
    score: 0.34192222222222224
    variance: 8.755555555555502e-07
    test_score: 0.6134
    ----------------------------------------------------------------------------------------------------
    evaluation run 2
    	dropout: 0.41645183851542744
    	embeddings: /home/axp797/axp797gallinahome/AnalyzeAccountability/.flair/embeddings/glove.gensim
    	hidden_size: 128
    	learning_rate: 0.15
    	mini_batch_size: 16
    	rnn_layers: 2
    score: 0.3705888888888889
    variance: 1.6962962962963451e-06
    test_score: 0.5806
    ----------------------------------------------------------------------------------------------------
    evaluation run 3
    	dropout: 0.06841856998276308
    	embeddings: glove.gensim
    	hidden_size: 128
    	learning_rate: 0.05
    	mini_batch_size: 8
    	rnn_layers: 1
    score: 0.3611666666666667
    variance: 1.370370370370381e-07
    test_score: 0.6006
    ----------------------------------------------------------------------------------------------------
    evaluation run 4
    	dropout: 0.43481261811291233
    	embeddings: en-fasttext-news-300d-1M
    	hidden_size: 64
    	learning_rate: 0.1
    	mini_batch_size: 32
    	rnn_layers: 1
    score: 0.4129777777777777
    variance: 1.5679259259259392e-05
    test_score: 0.4822
    ----------------------------------------------------------------------------------------------------
    evaluation run 5
    	dropout: 0.20850069217348033
    	embeddings: bpe-en-100000-50
    	hidden_size: 32
    	learning_rate: 0.1
    	mini_batch_size: 32
    	rnn_layers: 2
    score: 0.4092222222222222
    variance: 1.5851851851853048e-07
    test_score: 0.5348
    ----------------------------------------------------------------------------------------------------
    evaluation run 6
    	dropout: 0.31908978585395176
    	embeddings: en-fasttext-news-300d-1M
    	hidden_size: 128
    	learning_rate: 0.15
    	mini_batch_size: 8
    	rnn_layers: 2
    score: 0.3538666666666667
    variance: 2.4592592592592355e-07
    test_score: 0.6359
    ----------------------------------------------------------------------------------------------------
    evaluation run 7
    	dropout: 0.20295345479912913
    	embeddings: one-hot
    	hidden_size: 32
    	learning_rate: 0.1
    	mini_batch_size: 8
    	rnn_layers: 2
    score: 0.3832
    variance: 4.325925925926223e-07
    test_score: 0.6041
    ----------------------------------------------------------------------------------------------------


To produce these results, the code was run in an HPC, using a singularity container. The singularity recipe can be found in the [github](https://github.com/anjapago/AnalyzeAccountability/blob/master/singularity/Singularity).
