---
layout: post
title:  "Sentence Classifier with BERT"
date:   2019-07-11 00:00:30 -0400
categories: update
permalink: /:categories/:year/:month/:day/:title.html
---

This post will build on the baselines from the [previously tested](https://anjapago.github.io/AnalyzeAccountability/update/2019/06/05/binary-classifier.html) simple classifier methods, with the same objectives of calssifying accountability from excerpts of news articles.


## BERT CLassification Method




## Sentence Classifier Objectives

The objective is to be able to detect sentences about accountability from within a news article. The simplest approach to take for this would be to have a classifier that can operate sentence by sentence and output the classification of accountability or not. This approach can not be trained and tested given the existing dataset is in the form of excerpts ranging from 1-60 sentences in length. This dataset of excerpts has been transformed into single labelled sentences, and the previously tested simple classifiers will be re-tested on this new version of the dataset.

## Datasets

There are three versions of the data being tested:

1. The original excerpts: The original full length labelled excerpts were tested directly as is in the BERT classifier. Note since some are quite long, they would be truncated for use in BERT, the BERT model can only take in sequence lenghts of up to 128 tokens.
2. The excerpts that were only one sentence in length: There are about 6000 of these, which will be enough to make up a dataset of around 5000 for training and 1000 for testing. This should normally be sufficient, however due to the class imbalance of roughly 1:10 for accountability to non-accountability, the resulting test set will have only around 100 examples labelled with accountability.
3. The excerpts of less than five sentences. These excerpts were processed into the form of individually labelled sentences, where each sentence was given the label of the original excerpt. This produces a much larger dataset, of around 34000 sentences in total. This will result in a much larger test set of around 9000, and this would allow around 1000 samples in the test set to have the accountability label. This is a much larger test set, however this approach has introduced noise into the given labels, because some of the sentences now labelled as accountability may not actually clearly be about accountability, since it may have been a different sentence in the excerpt that was making the statement about accountability.


## Results

### Experimentation with the Original excerpts

There were a series of simple experiments run to test BERT classifier on the original dataset of excerpts. The experiments objectives were to figure out the following:

1. How to reduce over-fitting
2. How many epochs should be run
3. Does the full network need to be re-trained
4. How much variance is there in the performance measures based on the test/train split.
5. What combination of settings to run this classifier give the best results

The findings from each of these experiments will be explained in the following sections.

#### Experiment with Random State

These preliminary experiments involved running the code a few times with different random states in the test/train split. This was to get an idea how much the performance measures would vary just because of the way the data was split into the test and train set.

The findings were:

**random state = 0**

    {'auc': 0.8620361, 'eval_accuracy': 0.9392, 'f1_score': 0.77457625, 'false_negatives': 148.0, 'false_positives': 118.0, 'global_step': 1640, 'loss': 0.21235444, 'precision': 0.7947826, 'recall': 0.7553719, 'true_negatives': 3652.0, 'true_positives': 457.0}

**random state = 42**

    test = {'auc': 0.8757505, 'eval_accuracy': 0.9472, 'false_negatives': 130.0, 'false_positives': 101.0, 'global_step': 1640, 'loss': 0.20042753, 'precision': 0.81867146, 'recall': 0.778157, 'true_negatives': 3688.0, 'true_positives': 456.0}

These results show that for example, false negative and false positives can vary by as much as 20 test instances each just based on a change in the test/train split. This translated to a change of 0.03 in precision and 0.02 in recall.

Note, cross-validation could be used for more rigorous testing, but this could come at a cost of time. So, just keeping in mind, this amount of variability in the performance measures should be enough to correctly interpret future experimental results.

#### Experiment with regularization

The first observation noticed from running BERT classifier is that the performance measures on the training set is close to 100%, while on the test set it is quite low, around 0.6. This could be an indication of over-fitting. I tried various methods to improve this. The main method to try was experimenting with the dropout rate.

The drop out rate reduces the complexity of a neural net models, and therefore prevents over fitting. Drop out works by randomly removing network connections during the training. The higher the rate, the more the network is being generalized. In the BERT classifier, there is a setting called the Keep_rate, and this setting can be used to control how many nodes are preserved. IN this case, a keep rate close to 1 means very little regularization, while a keep rate close to 0.5 means around 50% of the nodes could be dropped.

Theoretically increasing the amount of regularization should increase the performance on the test set and decrease the performance on the training set until the two performance measures become closer together.

The results observed are shown in the chart below, with each performance measure indicating precision/recall.

| Dropout rate | Test Performance | Train Performance|
|--------------|------------------|------------------|
| 1 | 0.82/0.77 | 0.96/0.97 |
| 0.9 |0.82/0.78 | 0.96/0.97 |
| 0.8 | 0.80/0.77 | 0.96/0.97 |
| 0.6 | 0.80/0.77 | 0.96/0.97 |
| 0.4 | 0.82/0.76 | 0.96/0.97 |

The dropout value was changed a significant amount, however the changes in performance of both test and train were negligeable consider the variance of +/-0.3 possible in the performance measures (shown in the previous section).

While drop out it known to be the most appropriate regularization for this application, another regularization method called L2 regularization was also tested by adding L2 to the loss function in training the classifier, and in this case the performance was also not affected.

#### Experiment with number of epochs

#### Experiment with re-training the full network

#### Best Results

### Repeat Testing on Sentence excerpts

Using the same settings as was used to get the previous best results, BERT was re-run on the two labelled sentences datasets. The performance dropped significantly for both from the performance on the full excerpts. The results are significantly better than the simple classifiers though. The results for both versions of the sentence data set is shown below.

#### Single sentences

**Test Results:**

|   	|  True Label = 1 	|   True Label = 0	|
|---	|---	|---	|
| **Predicted Label = 1** 	| 51	| 14 |
| **Predicted Label = 0**	| 44 | 1037 |

**Tested on Train Data Results:**

|   	|  True Label = 1 	|   True Label = 0	|
|---	|---	|---	|
| **Predicted Label = 1** 	| 330 | 16 |
| **Predicted Label = 0**	| 21 | 4217 |

#### Short Excerpts of Less than 5 Sentences

**Test Results:**

|   	|  True Label = 1 	|   True Label = 0	|
|---	|---	|---	|
| **Predicted Label = 1** 	| 613	| 227 |
| **Predicted Label = 0**	| 347	| 5668 |

**Tested on Train Data Results:**

|   	|  True Label = 1 	|   True Label = 0	|
|---	|---	|---	|
| **Predicted Label = 1** 	| 3447| 238 |
| **Predicted Label = 0**	|  227	| 23507 |

#### Summary of Precision and Recall on Test Data

|   	|  Precision 	|   Recall	|
|---	|---	|---	|
| Single Sentences | 0.78 | 0.54 |
| Short Excerpts as sentences | 0.73 | 0.64 |
| Full Excerpts | 0.81 | 0.78 |

### Conclusions

* Overfitting
* Single Sentence vs Short excerpts
* Sentence Based vs Full excerpts
* BERT vs Simple classifiers

## Future Improvements

The biggest challenges in training this classifier is likely the noisy labels introduced in the sentence based classifier, and the class imbalance. Some approaches to address these issues in the future are shown in the following list.

* Using Multi-class classification:
* Adjusting loss function for class Imbalance
* Sample for class Imbalance
* Noise filter for noisy labels
