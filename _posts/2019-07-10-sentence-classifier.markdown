---
layout: post
title:  "Sentence Classifier Baselines"
date:   2019-07-10 00:00:30 -0400
categories: update
permalink: /:categories/:year/:month/:day/:title.html
---

This post will re-assess the [previously tested](https://anjapago.github.io/AnalyzeAccountability/update/2019/06/05/binary-classifier.html) simple classifier methods to establish a new baseline for the purposes of sentence classification.

## Sentence Classifier Objectives

The objective is to be able to detect sentences about accountability from within a news article. The simplest approach to take for this would be to have a classifier that can operate sentence by sentence and output the classification of accountability or not. This approach can not be trained and tested given the existing dataset is in the form of excerpts ranging from 1-60 sentences in length. This dataset of excerpts has been transformed into single labelled sentences, and the previously tested simple classifiers will be re-tested on this new version of the dataset.

## Datasets

There are two versions of the data being tested:

1. The excerpts that were only one sentence in length. There are about 6000 of these, which will be enough to make up a dataset of around 5000 for training and 1000 for testing. This should normally be sufficient, however due to the class imbalance of roughly 1:10 for accountability to non-accountability, the resulting test set will have only around 100 examples labelled with accountability.
2. The excerpts of less than five sentences. These excerpts were processed into the form of individually labelled sentences, where each sentence was given the label of the original excerpt. This produces a much larger dataset, of around 34000 sentences in total. This will result in a much larger test set of around 9000, and this would allow around 1000 samples in the test set to have the accountability label. This is a much larger test set, however this approach has introduced noise into the given labels, because some of the sentences now labelled as accountability may not actually clearly be about accountability, since it may have been a different sentence in the excerpt that was making the statement about accountability.


## Analysis of Baseline Classifiers

The three classifiers previously tested were re-tested with the same procedure as [before](https://anjapago.github.io/AnalyzeAccountability/update/2019/06/05/binary-classifier.html). These methods were chosen, because they are all commonly used methods in text classification. SVMs are known to be a strong baseline model, and logistic regression was included as another linear model for comparison. Random forest is an ensemble model capable of more complex, non-linear boundaries.

The results from all three models on both versions of the data was much worse than previous results, with both precision and recall dropping by about 0.1. The results are summarized in the following table. The results shown are precision/recall.

|   	| Single Sentences	| <5 Sentence Excerpts	|
|---	|---	|---	|
| SVM	| 0.46/0.54	| 0.72/0.36	|
| Logistic Regression	| 0.62/0.46	|  0.71/0.38	|
| Random Forest	| 0.71/0.32 | 0.73/0.51 |

To keep in mind, the total number of accountability labels in the test set for single single sentences was only around 100, so for example a difference of one or two examples can seemingly make a big difference in these scores - which can be highly affected by which examples are chosen by the test train split. I tested the test train split with multiple random states, and saw that these numbers are typically only accurate to around 0.05, though sometimes they can change quite a lot if it is an unlucky split. Keeping this level of accuracy in mind, the scores between the single sentences and the short excerpts of less than five sentences are quite similar overall. It is debatable which algorithm is the best performing, it depends on whether it is preferable to prioritize precision or recall, or wether a balance between the two is most preferable.

Comparing single sentences to short excerpts, it seems the short excerpts method would be best because the introduced label noise could be dealt with with label noise cleaning methods such as filters or label noise robust models. However using only the single sentence excerpts, not much could be done to improve those results because the dataset is just too small when considering the class imbalance.

## Classifiers Adjusted for Class Imbalance

One of the major issues hindering the performance of the classifier is the roughly 1:10 class imbalance of accountability to non-accountability labels. A simple first step was taken to address this, by using a weighted scoring function in the sklearn classifiers, to weight label errors proportionally to the class imbalance, to result in a more balanced contribution from each class. The effects are displayed in the table below, with precision/recall in the same way as the previous table.

|   	| Single Sentences	| <5 Sentence Excerpts	|
|---	|---	|---	|
| SVM	| 0.43/0.64	| 0.39/0.81	|
| Logistic Regression	| 0.42/0.74	|  0.40/0.80	|
| Random Forest	| 0.69/0.41 | 0.67/0.59 |

The most notable effect to observe, is that the the precision and recall scores for the short excerpts (<5 sentences) for the linear classifiers flipped, where the recall is now twice as high as the precision instead of the vice versa (in the previous chart). Also, the performance for random forest with short excerpts became more balanced between precision and recall. Overall the short excerpts once again seems a bit better than the single sentences.

Addressing the class imbalance with simple approach did not result in a major improvement in results, so more research will be required to address the issues present in the data.

## Future Performance Improvements

From the results of this data the main observations about what could lead to improvement in results is as follows:

1. Addressing the noisy labels: the performance has dropped significantly between the previous classifiers run on the full excerpts. The dataset of sentences made from excerpts of less than 5 sentences is now actually a bigger dataset with more examples than the previous dataset of full excerpts. Therefore the performance decrease in this case must be attributed to increasing the existing noise levels in the labels. There are many methods to address noisy labels, and so this could be experimented with as a promising approach to improve results.
2. Input representation: because the performance of all models was quite similar, with top scores averaging to around 0.5 in f1 score (the harmonic mean of precision and recall), this indicates that there is a limit on the success of a classifier given this input representation of the text (i.e. the a more complex classification method with a more complex boundary type is unlikely to make an improvement). It seems the issues come from too little meaning being captured in the input bag of words unigram representation. The next steps to improve this will be to experiment with pre-trained embedding models, and also test more approaches with the simple vectorizers, using bag of features (e.g. possibly including n-grams, and dimensions reductions).

These two areas seem to be the most likely approaches to improve results. Once some significant improvements has been seen, final steps to improve results would be tuning model hyper-parameters, and testing additional methods to deal with the class imbalance such as sampling.
