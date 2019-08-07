---
layout: post
title:  "Feature Importances of Tfidf Representations Classifiers"
date:   2019-08-03 00:00:30 -0400
categories: update
permalink: /:categories/:year/:month/:day/:title.html
---
This analysis will compare different text representations with simple sklearn linear and ensemble classifiers. The basis of all the text representations tested in this analysis is the sklearn vectorizer. The performance of these representations were tested in the [previous post](https://anjapago.github.io/AnalyzeAccountability/update/2019/08/01/vectorizer-comparison.html), and so the best performing methods from that analysis will be analyzed to determine which features (i.e. tokens or words) contribute to the decision to classify something as accountability. This will give further understanding into which method of text representation is most suitable for this task.


## Recap of Performance Results
The most notable effect on performance from the various representations was that character based consistently performed higher than other methods.

In the comparison of classifiers, it is clear overall the linear methods perform best, and the balanced linear classifiers was slightly better in most cases.

## Analysis of Features on performance

The following analysis will demonstrate which features contributed the most to the classification decision with various different representations. This can give an indication why some methods may be performing better that others, and also to see if the good performing methods have features that seem to related to the topic of accountability.

### Unigrams, Balanced

In the case of unigram, and balanced cost function, the features seem like they have some coherence with the topic of accountability, though do contain some event specific terms, such as the name "hornaday", that is most prevalent in a specific set of articles. This indicates that this representation seems like it would not generalize as well to new events.

#### Positive Features

|Weight | Feature|
---------|---------|
|+11.159	| hornaday|
|+10.813 | counsellor|
|+10.489	| bullied|
|+10.130	| rage|
|+9.911	| ugly|
|+9.760	| counselor|
|+9.615	| sprees|
|+8.979	| science|


#### Negative Features

|Weight | Feature|
---------|---------|
|-8.918 |	massacred|
|-9.079	| camera|
|-9.144	| marquez|
|-9.147	| stringent|
|-9.266	| animals|
|-9.279	| proposed|
|-9.763	| bills|
|-9.897	| apple|
|-10.262 |	undergo|
|-10.303	| peace|
|-11.353	| proposals|
|-13.895	| caption|

### Unigrams, Unbalanced

This representation seems to clearly demonstrate meaning related to accountability, with both the terms "blame" and "blamed" in the top most relevant terms to predict as positive for accountability. This may be indicating that despite the slightly higher performance in f-score from the balanced classifier, the unbalanced may actually be giving more meaningful results.

#### Positive Features

| Weight |	Feature |
|--------|----------|
| +5.122 | blame |
| +4.720 |	culture|
|+4.605	| blamed|
|+4.453	| shall|
|+4.126	| misogyny|
|+4.097	| counselor|
|+4.040	| rage|
|+3.882	| senselessness|
|+3.868	| isolated|
|+3.841	| hornaday|
|+3.795	| void|
|+3.795	| bullied|
|+3.788	| videos|
|+3.727	| none|
|+3.686	| illness|
|+3.664	| failure|
|+3.622	| counsellor|

#### Negative features

| Weight |	Feature |
|--------|----------|
|-3.843	| bmw |
|-3.935	| students|
|-4.184	| caption|

### Balanced, Character Based

The balanced character based was the best performing representation, though this is perplexing when analyzing the feature importances for the classifier. The features are not easily interpretable, and do not seem to clearly convey meaning.

#### Positive Features

|Weight	| Feature|
|-------|--------|
|+19.469	| e? |
|+19.191	| s? |
|+17.221	| n? |
|+16.696	| a? |
|+14.978	| fame|
|+13.483	| tered.|
|+13.476	| ak|
|+12.957	| ndw|
|+11.972	| be.|
|+11.777	|war,|
|+11.760	|var|
|+11.499	|u.|
|+11.329	| wild|
|+11.228	| se. |
|+11.153	|fame|
|+10.631	|od. |

#### Negative Features

| Weight |	Feature |
|--------|----------|
|-11.270	| spa|
|-11.304	| 6 |
|-12.947	| work |
|-13.294	| ?" |

### Balanced, Tri-grams

For classifiers incorporating 1-3 ngrams, the results are similar to the unbalanced unigram results. This method also did have a fairly good performance in f-score.

#### Positive Features

|Weight? | Feature|
|--------|--------|
|+10.839	| blame|
|+8.991	| in other|
|+8.746	| know this|
|+8.640	| knew he|
|+8.603	| jaylen|
|+8.571	| blamed|
|+8.456	| motives|
|+8.343	| culture|
|+8.291	| believe the|
|+8.232 |	fame|
|+8.226	| hornaday|
|+8.069	| he doesn|
|+8.020	| teens|
|+7.797	| women|

##### Negative features

| Weight |	Feature |
|--------|----------|
| -7.655	| marquez|
| -7.663	| apple|
| -7.784	| who was|
| -7.974	| jaylen fryberg|
| -8.451	| yes|
| -10.954	| caption|

## Conclusions

Methods that have the highest performance in f-score on the current datasets, do not necessarily have the best performance for generalizing to future unseen articles. To assess if the classifiers are capturing something meaningful, feature analysis is vary useful. From this analysis of feature importance, we can see that the highest performing methods: character based and balanced, are not capturing meaningful features specific to accountability. It seems from this analysis that unigrams and tri-grams methods were the capturing best meaning in the features.
